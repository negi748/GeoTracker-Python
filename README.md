GeoTracker-Python

A Python-based consent-based geolocation awareness dashboard with an optional Cloudflare Quick Tunnel integration.

Developer: negi748

Repository: https://github.com/negi748/GeoTracker-Python

---

Features

- Python-based geolocation awareness dashboard
- Browser-based local interface
- Consent-based location sharing
- Optional camera demonstration with explicit permission
- Automatic Cloudflare Quick Tunnel integration
- Automatic temporary public HTTPS URL generation
- Termux (Android) support
- Kali Linux support
- Local dashboard with temporary public access

---

Requirements

- Python 3
- Git
- Cloudflare "cloudflared"
- Modern web browser
- Internet connection

«"cloudflared" must be installed and available in the system PATH for automatic public-link generation.»

---

Installation

1. Clone the Repository

git clone https://github.com/negi748/GeoTracker-Python.git
cd GeoTracker-Python

2. Install Python Dependencies

If the repository contains a "requirements.txt" file:

pip install -r requirements.txt

If no "requirements.txt" file is included, use the dependencies documented by the project.

---

Run GeoTracker-Python

Start the application:

python GPS.py

The tool starts the local dashboard and automatically attempts to create a Cloudflare Quick Tunnel.

You should see output similar to:

GEO TRACKER

[+] Created by Negi

PRIVATE DASHBOARD (Local): http://127.0.0.1:8765/dashboard/...
LOCAL SHARE LINK: http://127.0.0.1:8765/share/...

[INFO] Generating public link via Cloudflare Tunnel...

Press CTRL+C to stop...

PUBLIC SHARE LINK: https://....trycloudflare.com/share/...

The generated PUBLIC SHARE LINK can then be opened in a browser.

---

How It Works

Python Application
        │
        ├── Local Dashboard
        │       │
        │       └── 127.0.0.1:<port>
        │
        └── Cloudflare Tunnel
                │
                └── Temporary HTTPS Public URL

The application runs locally first and then creates a temporary public URL through Cloudflare Tunnel.

---

Local Dashboard

The application provides a local dashboard through a localhost address similar to:

http://127.0.0.1:8765

The exact port and URL can vary depending on the application configuration.

---

Public Share Link

When Cloudflare Tunnel starts successfully, the application displays a temporary HTTPS URL similar to:

https://example-name.trycloudflare.com

The public URL is generated automatically by the application.

Important

- The URL is temporary.
- The URL can change when the application is restarted.
- Anyone who obtains the public URL may be able to access the exposed endpoint.
- Stop the application when testing is complete.
- Never expose private or sensitive information through a public tunnel.

---

Termux (Android)

Install the required packages:

pkg update
pkg install python git

Clone the repository:

git clone https://github.com/negi748/GeoTracker-Python.git
cd GeoTracker-Python

Install dependencies if required:

pip install -r requirements.txt

Run:

python GPS.py

If "cloudflared" is installed and available to the application, GeoTracker-Python will automatically attempt to create the public tunnel.

---

Kali Linux

Install Python and Git:

sudo apt update
sudo apt install python3 python3-pip git

Clone the repository:

git clone https://github.com/negi748/GeoTracker-Python.git
cd GeoTracker-Python

Install dependencies if required:

pip3 install -r requirements.txt

Run the application:

python3 GPS.py

The application will start the local dashboard and attempt to generate the temporary public Cloudflare URL automatically.

---

Cloudflare Tunnel

GeoTracker-Python can use Cloudflare Quick Tunnels to provide temporary HTTPS access to the locally running application.

Cloudflare documentation:

https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/do-more-with-tunnels/trycloudflare/

Automatic Process

You do not need to manually run:

cloudflared tunnel --url ...

when the application's automatic tunnel functionality is available.

The application handles the tunnel startup and displays the generated public URL in the terminal.

---

Privacy & Safety

This project should only be used for authorized development, testing, and educational purposes.

Before collecting location or camera data:

- Obtain explicit user consent.
- Clearly explain what information is collected.
- Only collect information necessary for the intended purpose.
- Never secretly track people.
- Never capture photos without permission.
- Never publish private user information.
- Never commit passwords, API keys, tokens, or other secrets to GitHub.

---

Security

Do not expose sensitive services through a public tunnel.

Avoid publishing:

- API keys
- Passwords
- Authentication tokens
- Private location data
- Personal information
- Private dashboard credentials

If you discover a security issue, report it responsibly rather than publishing sensitive exploit details publicly.

---

Project Structure

Example:

GeoTracker-Python/
│
├── GPS.py
├── README.md
├── .gitignore
└── requirements.txt

The exact structure may change as the project develops.

---

Troubleshooting

"python" command not found

Try:

python3 --version

---

"cloudflared" not found

Check:

cloudflared --version

Make sure "cloudflared" is installed and available in your system PATH.

---

Public link is not generated

Check:

1. Internet connection
2. "cloudflared" installation
3. "cloudflared --version"
4. Application terminal output
5. Local dashboard is running correctly

---

Local dashboard works but public URL does not

The application may be running correctly locally while the Cloudflare Tunnel component is unavailable.

Check the Cloudflare/"cloudflared" error shown in the terminal.

---

Development

Contributions and improvements are welcome.

When contributing:

1. Test your changes locally.
2. Do not commit secrets.
3. Update documentation when functionality changes.
4. Respect user privacy and consent.

---

License

MIT License

Copyright (c) 2026 negi748

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

---

Author

negi748

GitHub:

https://github.com/negi748

GeoTracker-Python:

https://github.com/negi748/GeoTracker-Python

---

Disclaimer

GeoTracker-Python is intended for authorized development, testing, and educational use.

Use the software responsibly and obtain appropriate consent before collecting personal information such as location or camera data.
