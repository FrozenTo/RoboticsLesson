# Smart Solutions Lab 2 — local post-office server

This is the first software-only implementation of the Lab 2 public-server workflow. It does **not** control the MG400 directly. The Atom/station side will later receive only approved whole jobs.

## Implemented

- password-protected user page (HTTP Basic auth for the local Flask app);
- strict allowed-job list: 'letter', 'pick_place', 'display_test';
- pending-job expiration;
- Atom Bearer-token authentication;
- Atom polling / heartbeat (last_seen, robot state, optional pressure);
- one-time dispatch of the oldest pending job;
- done / refused result reporting;
- SQLite persistence;
- /healthz endpoint for deployment checks.

**Status:** implemented and syntax-checked. It has not yet been run with Flask on the team PC, deployed to the Ubuntu droplet, or tested with AtomS3, the station or MG400.

## Run on Windows first

From Nutilahendused/lab2/server in PowerShell:

~~~powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

$env:SMARTLAB_USER="team"
$env:SMARTLAB_USER_PASSWORD="choose-a-local-test-password"
$env:SMARTLAB_ATOM_TOKEN="choose-a-separate-local-test-token"
$env:SMARTLAB_JOB_TTL_SECONDS="60"

python app.py
~~~

Open http://127.0.0.1:5000/. The browser will ask for the configured username/password.

Do **not** commit the real password or Atom token. On the droplet these values should be supplied through the service environment, not source code.

## Simulate the Atom from another PowerShell window

Set the same temporary Atom token in the second window and poll the server:

~~~powershell
$env:SMARTLAB_ATOM_TOKEN="choose-a-separate-local-test-token"
$headers = @{ Authorization = "Bearer $env:SMARTLAB_ATOM_TOKEN" }
$body = @{ device = "team-atom"; robot = "ready"; p = -52.3 } | ConvertTo-Json

Invoke-RestMethod -Method Post -Uri http://127.0.0.1:5000/api/atom/poll -Headers $headers -ContentType "application/json" -Body $body
~~~

With no queued work the response should contain msg = null.

After submitting a job in the browser, run the same command again. The response should contain msg, job, arg, timestamps and expiration.

Report success:

~~~powershell
$result = @{ msg = 1; result = "done" } | ConvertTo-Json
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:5000/api/atom/result -Headers $headers -ContentType "application/json" -Body $result
~~~

Replace 1 with the real message ID.

## Safety behavior

The server never accepts coordinates, speeds, shell commands or arbitrary code. A server job is only a named, allow-listed complete task. Actual robot-state validation remains the responsibility of the Atom/station integration before any MG400 command is sent.

A dispatched job is not automatically re-delivered if communication disappears. This avoids accidentally executing the same robot task twice. Recovery behavior will be tested later with the real Atom/station workflow.
