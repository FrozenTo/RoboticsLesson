from __future__ import annotations

import hmac
import os
import sqlite3
from datetime import datetime, timedelta, timezone
from functools import wraps
from pathlib import Path
from typing import Any, Callable, TypeVar

from flask import Flask, Response, g, jsonify, render_template, request

F = TypeVar("F", bound=Callable[..., Any])

DEFAULT_DB_PATH = Path(__file__).with_name("postoffice.db")
DEFAULT_JOB_TTL_SECONDS = 60
ALLOWED_JOBS = {"letter", "pick_place", "display_test"}
FINAL_STATES = {"done", "refused", "expired"}


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(value: datetime | None = None) -> str:
    return (value or utc_now()).isoformat(timespec="seconds")


def create_app(test_config: dict[str, Any] | None = None) -> Flask:
    app = Flask(__name__)
    app.config.update(
        DATABASE=os.getenv("SMARTLAB_DB", str(DEFAULT_DB_PATH)),
        USERNAME=os.getenv("SMARTLAB_USER", "team"),
        USER_PASSWORD=os.getenv("SMARTLAB_USER_PASSWORD", ""),
        ATOM_TOKEN=os.getenv("SMARTLAB_ATOM_TOKEN", ""),
        JOB_TTL_SECONDS=int(
            os.getenv("SMARTLAB_JOB_TTL_SECONDS", DEFAULT_JOB_TTL_SECONDS)
        ),
    )
    if test_config:
        app.config.update(test_config)

    def get_db() -> sqlite3.Connection:
        if "db" not in g:
            db = sqlite3.connect(app.config["DATABASE"])
            db.row_factory = sqlite3.Row
            g.db = db
        return g.db

    def init_db() -> None:
        db = get_db()
        db.executescript(
            """
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job TEXT NOT NULL,
                arg TEXT,
                state TEXT NOT NULL,
                created_at TEXT NOT NULL,
                expires_at TEXT NOT NULL,
                dispatched_at TEXT,
                finished_at TEXT,
                result TEXT,
                why TEXT
            );

            CREATE TABLE IF NOT EXISTS atom_state (
                device TEXT PRIMARY KEY,
                last_seen TEXT NOT NULL,
                robot_state TEXT,
                pressure_kpa REAL
            );
            """
        )
        db.commit()

    @app.teardown_appcontext
    def close_db(_: BaseException | None) -> None:
        db = g.pop("db", None)
        if db is not None:
            db.close()

    def user_authorized() -> bool:
        configured = str(app.config["USER_PASSWORD"])
        if not configured:
            return False
        auth = request.authorization
        if not auth:
            return False
        return hmac.compare_digest(
            auth.username or "", str(app.config["USERNAME"])
        ) and hmac.compare_digest(auth.password or "", configured)

    def require_user_auth(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            if not user_authorized():
                return Response(
                    "Authentication required",
                    401,
                    {"WWW-Authenticate": 'Basic realm="Smart Lab 2"'},
                )
            return func(*args, **kwargs)

        return wrapper  # type: ignore[return-value]

    def atom_authorized() -> bool:
        configured = str(app.config["ATOM_TOKEN"])
        if not configured:
            return False
        header = request.headers.get("Authorization", "")
        if not header.startswith("Bearer "):
            return False
        supplied = header.removeprefix("Bearer ").strip()
        return hmac.compare_digest(supplied, configured)

    def require_atom_auth(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any):
            if not atom_authorized():
                return jsonify({"error": "unauthorized"}), 401
            return func(*args, **kwargs)

        return wrapper  # type: ignore[return-value]

    def expire_pending_jobs(db: sqlite3.Connection) -> int:
        now = iso_utc()
        cursor = db.execute(
            """
            UPDATE jobs
               SET state = 'expired', finished_at = ?
             WHERE state = 'pending' AND expires_at <= ?
            """,
            (now, now),
        )
        db.commit()
        return cursor.rowcount

    def validate_job(job: str, arg: Any) -> tuple[bool, str | None, str | None]:
        if job not in ALLOWED_JOBS:
            return False, None, f"unsupported job: {job}"

        if job == "letter":
            letter = str(arg or "").strip().upper()
            if len(letter) != 1 or not ("A" <= letter <= "Z"):
                return False, None, "letter job requires one A-Z character"
            return True, letter, None

        if job in {"pick_place", "display_test"}:
            if arg not in (None, "", {}):
                return False, None, f"{job} does not accept an argument"
            return True, None, None

        return False, None, "invalid job"

    def latest_atom(db: sqlite3.Connection) -> dict[str, Any] | None:
        row = db.execute(
            """
            SELECT device, last_seen, robot_state, pressure_kpa
              FROM atom_state
             ORDER BY last_seen DESC
             LIMIT 1
            """
        ).fetchone()
        return dict(row) if row else None

    def job_to_dict(row: sqlite3.Row) -> dict[str, Any]:
        return {
            "id": row["id"],
            "job": row["job"],
            "arg": row["arg"],
            "state": row["state"],
            "created_at": row["created_at"],
            "expires_at": row["expires_at"],
            "dispatched_at": row["dispatched_at"],
            "finished_at": row["finished_at"],
            "result": row["result"],
            "why": row["why"],
        }

    @app.get("/")
    @require_user_auth
    def index():
        db = get_db()
        expire_pending_jobs(db)
        jobs = db.execute(
            "SELECT * FROM jobs ORDER BY id DESC LIMIT 25"
        ).fetchall()
        return render_template(
            "index.html",
            jobs=[job_to_dict(row) for row in jobs],
            atom=latest_atom(db),
            allowed_jobs=sorted(ALLOWED_JOBS),
            ttl=app.config["JOB_TTL_SECONDS"],
        )

    @app.get("/healthz")
    def healthz():
        return jsonify({"status": "ok"})

    @app.post("/api/jobs")
    @require_user_auth
    def create_job():
        payload = request.get_json(silent=True) or request.form.to_dict()
        job = str(payload.get("job", "")).strip()
        valid, normalized_arg, error = validate_job(job, payload.get("arg"))
        if not valid:
            return jsonify(
                {"error": error, "allowed_jobs": sorted(ALLOWED_JOBS)}
            ), 400

        created = utc_now()
        expires = created + timedelta(
            seconds=int(app.config["JOB_TTL_SECONDS"])
        )
        db = get_db()
        cursor = db.execute(
            """
            INSERT INTO jobs(job, arg, state, created_at, expires_at)
            VALUES (?, ?, 'pending', ?, ?)
            """,
            (job, normalized_arg, iso_utc(created), iso_utc(expires)),
        )
        db.commit()
        row = db.execute(
            "SELECT * FROM jobs WHERE id = ?", (cursor.lastrowid,)
        ).fetchone()
        return jsonify(job_to_dict(row)), 201

    @app.get("/api/jobs")
    @require_user_auth
    def list_jobs():
        db = get_db()
        expire_pending_jobs(db)
        rows = db.execute(
            "SELECT * FROM jobs ORDER BY id DESC LIMIT 100"
        ).fetchall()
        return jsonify({"jobs": [job_to_dict(row) for row in rows]})

    @app.post("/api/atom/poll")
    @require_atom_auth
    def atom_poll():
        payload = request.get_json(silent=True) or {}
        device = str(payload.get("device", "")).strip()
        if not device or len(device) > 80:
            return jsonify(
                {"error": "device is required (max 80 characters)"}
            ), 400

        robot_state = payload.get("robot")
        pressure = payload.get("p")
        if pressure is not None:
            try:
                pressure = float(pressure)
            except (TypeError, ValueError):
                return jsonify({"error": "p must be numeric or null"}), 400

        db = get_db()
        now = iso_utc()
        db.execute(
            """
            INSERT INTO atom_state(device, last_seen, robot_state, pressure_kpa)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(device) DO UPDATE SET
                last_seen = excluded.last_seen,
                robot_state = excluded.robot_state,
                pressure_kpa = excluded.pressure_kpa
            """,
            (
                device,
                now,
                None if robot_state is None else str(robot_state),
                pressure,
            ),
        )
        expire_pending_jobs(db)

        row = db.execute(
            """
            SELECT *
              FROM jobs
             WHERE state = 'pending'
             ORDER BY id ASC
             LIMIT 1
            """
        ).fetchone()
        if row is None:
            db.commit()
            return jsonify({"msg": None, "server_time": now})

        db.execute(
            """
            UPDATE jobs
               SET state = 'dispatched', dispatched_at = ?
             WHERE id = ?
            """,
            (now, row["id"]),
        )
        db.commit()
        return jsonify(
            {
                "msg": row["id"],
                "job": row["job"],
                "arg": row["arg"],
                "left": row["created_at"],
                "expires_at": row["expires_at"],
                "server_time": now,
            }
        )

    @app.post("/api/atom/result")
    @require_atom_auth
    def atom_result():
        payload = request.get_json(silent=True) or {}
        try:
            msg_id = int(payload.get("msg"))
        except (TypeError, ValueError):
            return jsonify({"error": "msg must be an integer"}), 400

        result = str(payload.get("result", "")).strip().lower()
        if result not in {"done", "refused"}:
            return jsonify(
                {"error": "result must be done or refused"}
            ), 400
        why = payload.get("why")
        if why is not None:
            why = str(why)[:500]

        db = get_db()
        row = db.execute(
            "SELECT * FROM jobs WHERE id = ?", (msg_id,)
        ).fetchone()
        if row is None:
            return jsonify({"error": "unknown message"}), 404
        if row["state"] in FINAL_STATES:
            return jsonify(
                {"error": f"message already final: {row['state']}"}
            ), 409
        if row["state"] != "dispatched":
            return jsonify(
                {"error": f"message is not dispatched: {row['state']}"}
            ), 409

        finished = iso_utc()
        db.execute(
            """
            UPDATE jobs
               SET state = ?, result = ?, why = ?, finished_at = ?
             WHERE id = ?
            """,
            (result, result, why, finished, msg_id),
        )
        db.commit()
        return jsonify(
            {
                "msg": msg_id,
                "result": result,
                "why": why,
                "finished_at": finished,
            }
        )

    @app.get("/api/status")
    @require_user_auth
    def status():
        db = get_db()
        expire_pending_jobs(db)
        return jsonify(
            {
                "atom": latest_atom(db),
                "allowed_jobs": sorted(ALLOWED_JOBS),
            }
        )

    with app.app_context():
        init_db()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
