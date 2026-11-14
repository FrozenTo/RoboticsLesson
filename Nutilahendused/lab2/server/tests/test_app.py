import base64
import tempfile
import unittest
from pathlib import Path

from app import create_app


class PostOfficeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        db = Path(self.tmp.name) / "test.db"
        self.app = create_app(
            {
                "TESTING": True,
                "DATABASE": str(db),
                "USERNAME": "team",
                "USER_PASSWORD": "pw",
                "ATOM_TOKEN": "atom-secret",
                "JOB_TTL_SECONDS": 60,
            }
        )
        self.client = self.app.test_client()
        token = base64.b64encode(b"team:pw").decode()
        self.user_headers = {"Authorization": f"Basic {token}"}
        self.atom_headers = {"Authorization": "Bearer atom-secret"}

    def tearDown(self):
        self.tmp.cleanup()

    def test_health(self):
        response = self.client.get("/healthz")
        self.assertEqual(response.status_code, 200)

    def test_user_auth_required(self):
        self.assertEqual(self.client.get("/").status_code, 401)

    def test_unknown_job_is_rejected(self):
        response = self.client.post(
            "/api/jobs",
            json={"job": "move_xyz", "arg": "10,20,30"},
            headers=self.user_headers,
        )
        self.assertEqual(response.status_code, 400)

    def test_letter_is_normalized_and_dispatched_once(self):
        created = self.client.post(
            "/api/jobs",
            json={"job": "letter", "arg": "k"},
            headers=self.user_headers,
        )
        self.assertEqual(created.status_code, 201)
        self.assertEqual(created.get_json()["arg"], "K")

        poll = self.client.post(
            "/api/atom/poll",
            json={"device": "atom-1", "robot": "ready", "p": -52.3},
            headers=self.atom_headers,
        )
        data = poll.get_json()
        self.assertEqual(data["job"], "letter")
        self.assertEqual(data["arg"], "K")
        msg = data["msg"]

        second = self.client.post(
            "/api/atom/poll",
            json={"device": "atom-1", "robot": "ready"},
            headers=self.atom_headers,
        )
        self.assertIsNone(second.get_json()["msg"])

        result = self.client.post(
            "/api/atom/result",
            json={"msg": msg, "result": "done"},
            headers=self.atom_headers,
        )
        self.assertEqual(result.status_code, 200)

    def test_atom_token_required(self):
        response = self.client.post(
            "/api/atom/poll",
            json={"device": "atom-1"},
        )
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
