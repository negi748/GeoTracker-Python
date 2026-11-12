🌐 GeoTracker-Python

A Python-based consent-based geolocation awareness dashboard designed for authorized development, testing, and educational purposes.

Developer: "negi748" (https://github.com/negi748)

Repository: "GeoTracker-Python" (https://github.com/negi748/GeoTracker-Python)

---

✨ Features

- 🐍 Python-based web dashboard
- 🌐 Browser-based interface
- 📍 Consent-based location sharing
- 📷 Optional camera demonstration with explicit permission
- ☁️ Automatic Cloudflare Tunnel integration
- 🔗 Automatic temporary public HTTPS share link
- 📱 Termux (Android) support
- 🐉 Kali Linux support
- 🖥️ Local dashboard
- 🔒 Privacy-focused usage
- ⚡ Simple command-line startup

---

📋 Requirements

Before running GeoTracker-Python, make sure your system has:

- Python 3
- Git
- "cloudflared"
- Modern web browser
- Internet connection

«"cloudflared" must be installed and available to the application for automatic public-link generation.»

---

⚡ Quick Start

📱 Termux

Copy the command below and paste it into Termux:

git clone https://github.com/negi748/GeoTracker-Python.git && cd GeoTracker-Python && (test -f requirements.txt && pip install -r requirements.txt || true) && python GPS.py

Press Enter.

The project will be cloned, dependencies will be installed if "requirements.txt" exists, and the application will start.

---

🐉 Kali Linux

Copy the command below and paste it into Kali Linux:

git clone https://github.com/negi748/GeoTracker-Python.git && cd GeoTracker-Python && (test -f requirements.txt && pip3 install -r requirements.txt || true) && python3 GPS.py

Press Enter.

The project will be cloned, dependencies will be installed if "requirements.txt" exists, and the application will start.

---

🔧 Manual Installation

If you prefer to install the project step by step, follow the instructions below.

1. Clone the Repository

git clone https://github.com/negi748/GeoTracker-Python.git

2. Enter the Project Directory

cd GeoTracker-Python

3. Install Dependencies

If the repository contains "requirements.txt":

pip install -r requirements.txt

For systems using "pip3":

pip3 install -r requirements.txt

4. Start the Application

python GPS.py

Or:

python3 GPS.py

---

☁️ Automatic Cloudflare Tunnel

GeoTracker-Python can automatically use Cloudflare Tunnel to create a temporary public HTTPS URL.

You do not need to manually run a Cloudflare tunnel command when the automatic tunnel feature is available.

After starting the application, the terminal will display information similar to:

[INFO] Generating public link via Cloudflare Tunnel...

Press CTRL+C to stop...

PUBLIC SHARE LINK: https://example-name.trycloudflare.com/share/...

Copy the displayed PUBLIC SHARE LINK and open it in your browser.

---

🔄 How It Works

Run "GPS.py"
↓
Python Web Server
↓
Local Dashboard
↓
Cloudflare Tunnel
↓
Temporary HTTPS URL
↓
PUBLIC SHARE LINK

The application starts the local server and then uses Cloudflare Tunnel to provide temporary public access when the tunnel component is available.

---

🖥️ Local Dashboard

The application runs a local web dashboard.

Example:

http://127.0.0.1:8765

The exact port may vary depending on the application configuration.

The application displays the actual local address when it starts.

---

🔗 Public Share Link

When Cloudflare Tunnel starts successfully, the terminal displays a temporary HTTPS URL similar to:

https://example-name.trycloudflare.com/share/...

The public URL:

- Is temporary
- Can change after restarting the application
- Works only while the application/tunnel is running
- Should only be shared with authorized users

---

📱 Termux Installation

Update Packages

pkg update

Install Python and Git

pkg install python git

Clone GeoTracker-Python

git clone https://github.com/negi748/GeoTracker-Python.git

Enter the Directory

cd GeoTracker-Python

Install Python Dependencies

If "requirements.txt" exists:

pip install -r requirements.txt

Start the Tool

python GPS.py

If "cloudflared" is installed and available to the application, GeoTracker-Python will automatically attempt to generate the public share link.

---

🐉 Kali Linux Installation

Update Packages

sudo apt update

Install Python and Git

sudo apt install python3 python3-pip git

Clone GeoTracker-Python

git clone https://github.com/negi748/GeoTracker-Python.git

Enter the Directory

cd GeoTracker-Python

Install Dependencies

pip3 install -r requirements.txt

Start the Tool

python3 GPS.py

The application will start the local dashboard and attempt to generate the temporary public Cloudflare URL automatically.

---

☁️ Cloudflare Requirements

Check whether "cloudflared" is installed:

cloudflared --version

If the command works, the application can use the installed Cloudflare client for its automatic tunnel functionality.

Official Cloudflare documentation:

https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/do-more-with-tunnels/trycloudflare/

---

⚠️ Public Tunnel Warning

A Cloudflare Tunnel can make a locally running application accessible through the internet.

Therefore:

- Do not expose private services.
- Do not expose sensitive dashboards.
- Do not publish passwords or API keys.
- Do not share public URLs unnecessarily.
- Stop the application when testing is complete.

Press:

CTRL + C

to stop the application and its active tunnel.

---

🔐 Privacy & Safety

GeoTracker-Python is intended for authorized development, testing, and educational use.

Before collecting location or camera data:

- Obtain explicit user consent.
- Clearly explain what information is collected.
- Only collect information necessary for the intended purpose.
- Never secretly track people.
- Never capture photos without permission.
- Never publish private user information.
- Never commit passwords, API keys, access tokens, or secrets to GitHub.

---

🛡️ Security

Do not expose sensitive services through a public tunnel.

Never commit or publish:

- API keys
- Passwords
- Authentication tokens
- Private location data
- Personal information
- Cloudflare credentials
- Private configuration files

Keep sensitive information outside the repository.

---

🛠️ Troubleshooting

Python is not installed

Check:

python --version

Or:

python3 --version

---

Git is not installed

Check:

git --version

---

Cloudflared is not found

Check:

cloudflared --version

Make sure "cloudflared" is installed and available in the system PATH.

---

"requirements.txt" not found

Check the project files:

ls

If "requirements.txt" does not exist, do not run:

pip install -r requirements.txt

Use the dependencies required by the current project implementation.

---

Public URL is not generated

Check:

1. Internet connection
2. "cloudflared" installation
3. "cloudflared --version"
4. Terminal error messages
5. Local dashboard startup

The local application must be running before a public tunnel can be created.

---

Local Dashboard Works but Public Link Does Not

The Python application may be running correctly while the Cloudflare Tunnel component is unavailable.

Check the terminal output for the specific "cloudflared" error.

---

📂 Project Structure

GeoTracker-Python/
│
├── GPS.py
├── README.md
├── .gitignore
└── requirements.txt

The exact structure may change as the project is updated.

---

🚀 Development

Contributions and improvements are welcome.

Before submitting changes:

1. Test the application locally.
2. Keep secrets out of the repository.
3. Update the README when functionality changes.
4. Respect user privacy and consent.
5. Do not submit private or sensitive data.

---

📜 License

MIT License

Copyright (c) 2026 negi748

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, subject to the following
conditions:

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

👤 Author

negi748

GitHub Profile:

https://github.com/negi748

Project:

https://github.com/negi748/GeoTracker-Python

---

⚠️ Disclaimer

GeoTracker-Python is provided for authorized development, testing, and educational purposes.

Use this software responsibly and obtain appropriate permission and informed consent before collecting personal information such as location or camera data.
