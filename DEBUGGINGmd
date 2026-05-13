## Lab 3: Troubleshooting & Fixes

## 1. Frontend Logic Error (index.html)
* **Symptom:** The webpage loaded, but the greeting message did not display.
* **Root Cause:** That `<h1>` tag on line 9 was left unclosed, causing the browser to misinterpret the trailing JavaScript block. 
* **Fix:** Properly closed the `<h1 id="greeting-display">` tag and separated the async `fetch()` logic into a distinct script block.

## 2. Infrastructure Connectivity (Security Groups)
* **Symptom:** EC2 Instance Connect failed with a "Failed to connect" error.
* **Root Cause:** The AWS Security Group (cpga2025-sg) lacked an inbound (I didn't double check) rule for Port 22. 
* **Fix:** Added an Inbound Rule allowing SSH (Port 22) traffic from Anywhere-IPv4 to enable terminal access.

## 3. Server-Side Execution (app.py)
* **Symptom:** Browser returned an `ERR_EMPTY_RESPONSE` and `CONNECTION_CLOSED`.
* **Root Cause:** The original `app.py` was a basic Python script, not a web server. When executed, it printed to the console and terminated.
* **Fix:** Refactored `app.py` into a Flask application listening on `host='0.0.0.0'` and used `nohup` to run the process persistently in the background.
