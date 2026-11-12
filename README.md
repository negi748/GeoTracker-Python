GeoTracker-Python

A Python-based consent-based geolocation awareness dashboard for development, testing, and educational purposes.

Developer: "negi748" (https://github.com/negi748)

Repository: https://github.com/negi748/GeoTracker-Python

---

Features

- Python-based web dashboard
- Browser-based interface
- Consent-based location sharing
- Optional camera demonstration with explicit permission
- Automatic Cloudflare Tunnel integration
- Automatic temporary public HTTPS URL
- Termux (Android) support
- Kali Linux support
- Local dashboard
- Temporary public share link

---

Requirements

- Python 3
- Git
- "cloudflared"
- Modern web browser
- Internet connection

«"cloudflared" must be installed and available to the application for automatic public-link generation.»

---

⚡ Quick Installation

📱 Termux

Copy and paste the following command:

git clone https://github.com/negi748/GeoTracker-Python.git && cd GeoTracker-Python && (test -f requirements.txt && pip install -r requirements.txt || true) && python GPS.py

Press Enter and the application will start.

---

🐉 Kali Linux

Copy and paste:

git clone https://github.com/negi748/GeoTracker-Python.git && cd GeoTracker-Python && (test -f requirements.txt && pip3 install -r requirements.txt || true) && python3 GPS.py

Press Enter and the application will start.

---

🔧 Manual Installation

If you prefer to install the project step by step:

1. Clone the Repository

git clone https://github.com/negi748/GeoTracker-Python.git

2. Enter the Project Directory

cd GeoTracker-Python

3. Install Python Dependencies

If "requirements.txt" exists:

pip install -r requirements.txt

For systems using "pip3":

pip3 install -r requirements.txt

4. Start GeoTracker-Python

python GPS.py

Or:

python3 GPS.py

---

☁️ Automatic Cloudflare Tunnel

GeoTracker-Python can automatically use "cloudflared" to create a temporary public HTTPS URL.

You do not need to manually start the tunnel when the automatic tunnel feature is available.

After starting the application, the terminal will display information similar to:

[INFO] Generating public link via Cloudflare Tunnel...

Press CTRL+C to stop...

PUBLIC SHARE LINK: https://example-name.trycloudflare.com/share/...

Copy the displayed PUBLIC SHARE LINK and open it in your browser.

Example Flow

python GPS.py
      │
      ▼
Local Dashboard
      │
      ▼
Cloudflare Tunnel
      │
      ▼
Temporary HTTPS URL
      │
      ▼
PUBLIC SHARE LINK

---

📱 Termux Setup

Install Python and Git:

pkg update
pkg install python git

Clone the project:

git clone https://github.com/negi748/GeoTracker-Python.git
cd GeoTracker-Python

Install dependencies if required:

pip install -r requirements.txt

Start the application:

python GPS.py

If "cloudflared" is correctly installed and available, the application will automatically attempt to create the public tunnel.

---

🐉 Kali Linux Setup

Update packages:

sudo apt update

Install Python and Git:

sudo apt install python3 python3-pip git

Clone the project:

git clone https://github.com/negi748/GeoTracker-Python.git
cd GeoTracker-Python

Install dependencies:

pip3 install -r requirements.txt

Start the application:

python3 GPS.py

The application will start the local dashboard and attempt to generate the temporary public Cloudflare URL automatically.

---

🌐 Local Dashboard

The application runs a local web dashboard.

Example:

http://127.0.0.1:8765

The exact port may vary depending on the application configuration.

The terminal displays the actual local address when the application starts.

---

🔗 Public Share Link

When Cloudflare Tunnel starts successfully, GeoTracker-Python displays a temporary HTTPS URL similar to:

https://example-name.trycloudflare.com/share/...

The public URL:

- Is temporary
- Can change after restarting the application
- Requires the application and tunnel to remain running
- Should only be shared with authorized users

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
- Never commit passwords, API keys, tokens, or secrets to GitHub.

---

⚠️ Public Tunnel Warning

A Cloudflare Tunnel can make a locally running application accessible from the internet.

Therefore:

- Do not expose sensitive services.
- Do not expose private dashboards.
- Do not publish credentials.
- Do not share the public URL unnecessarily.
- Stop the application when testing is finished.

Press:

CTRL + C

to stop the application and its active tunnel.

---

🛠️ Troubleshooting

Python not found

Check:

python --version

or:

python3 --version

---

Git not found

Check:

git --version

Install Git if necessary.

---

cloudflared not found

Check:

cloudflared --version

Make sure "cloudflared" is installed and available in the system PATH.

---

"requirements.txt" not found

Check the project files:

ls

If "requirements.txt" does not exist, do not run:

pip install -r requirements.txt

The project should be run using the dependencies required by the current implementation.

---

Public URL is not generated

Check:

1. Internet connection
2. "cloudflared" installation
3. "cloudflared --version"
4. Terminal error messages
5. Local dashboard startup

The local application should be running before a public tunnel can be created.

---

📂 Project Structure

GeoTracker-Python/
│
├── GPS.py
├── README.md
├── .gitignore
└── requirements.txt

The exact project structure may change as the project is updated.

---

🚀 Development

Contributions and improvements are welcome.

Before submitting changes:

1. Test the application locally.
2. Keep secrets out of the repository.
3. Update the README when functionality changes.
4. Respect user privacy and consent.

---

📜 License

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

👤 Author

negi748

GitHub:

https://github.com/negi748

Project:

https://github.com/negi748/GeoTracker-Python

---

Disclaimer

GeoTracker-Python is provided for authorized development, testing, and educational purposes.

Use this software responsibly and obtain appropriate permission and informed consent before collecting personal information such as location or camera data.
