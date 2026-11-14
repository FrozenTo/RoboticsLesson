# Smart Solutions Lab 2 — server API

**Status:** first local implementation, 14.11.2026. Software-only code is prepared; real Atom/MG400 integration is still TODO.

The public server acts as a **post office**. It does not send motion commands to the MG400. A user leaves a complete approved job; the Atom polls the server and later reports the result.

## Authentication

- User/browser endpoints use HTTP Basic authentication in this first implementation.
- Atom endpoints require an Authorization: Bearer <token> header.
- Real passwords and tokens are environment variables and must not be committed to Git.
- HTTPS is required before exposing authenticated endpoints on the public droplet.

## Allowed jobs

| Job | Argument | Meaning |
| --- | --- | --- |
| letter | one A–Z character | draw an approved letter trajectory |
| pick_place | none | run the approved pick/place task |
| display_test | none | run an Atom display test |

This is an allow-list. Coordinates, robot speed, shell commands and arbitrary code are not accepted.

## User endpoints

### GET /

Password-protected status page. Shows the latest Atom heartbeat, a job form and recent jobs.

### POST /api/jobs

Creates one approved job.

Example:

~~~json
{"job":"letter","arg":"K"}
~~~

The server adds an ID, creation time and expiration time. The current development TTL defaults to 60 seconds and is configurable with SMARTLAB_JOB_TTL_SECONDS. This is a software setting, not a measured latency result.

Unknown jobs return HTTP 400 and are never queued.

### GET /api/jobs

Returns recent jobs for the authenticated user.

### GET /api/status

Returns latest Atom state and the allowed-job list for the authenticated user.

## Atom endpoints

### POST /api/atom/poll

Atom sends its state and asks for work.

Request example:

~~~json
{"device":"team-atom","robot":"ready","p":-52.3}
~~~

If there is no job:

~~~json
{"msg":null,"server_time":"..."}
~~~

If there is a pending non-expired job:

~~~json
{
  "msg":17,
  "job":"letter",
  "arg":"K",
  "left":"...",
  "expires_at":"...",
  "server_time":"..."
}
~~~

When returned to the Atom, the job changes from pending to dispatched. It is not automatically delivered again. This is deliberate: repeating a complete robot job after a network timeout could cause duplicate motion.

The poll also updates the Atom heartbeat: device, last_seen, robot_state and optional pressure.

### POST /api/atom/result

Reports the result of a dispatched message.

Successful result:

~~~json
{"msg":17,"result":"done"}
~~~

Refusal:

~~~json
{"msg":17,"result":"refused","why":"robot not enabled"}
~~~

Allowed final results are done and refused. The server records completion time and the optional reason.

## Job states

~~~text
pending -> dispatched -> done
                    -> refused
pending -> expired
~~~

Only a pending job can expire automatically. A dispatched job is never silently re-run.

## Still to implement/test

- run the Flask application locally on the team Windows PC;
- deploy it to the existing Ubuntu droplet;
- configure Flask as a service behind HTTPS/Caddy;
- open only required 80/443 firewall ports when deployment is ready;
- connect a real Atom poller;
- connect Atom to the station/MG400 job executor;
- verify stale/expired-job behavior on real hardware;
- test connection loss during an already-running job;
- measure the required 30-job latency sets at two polling intervals;
- define/test the final Atom-off stale threshold on the web page;
- integrate final pressure calibration/settings after Data Acquisition is complete;
- integrate camera feeds locally after the 3D-printed mounts are ready.
