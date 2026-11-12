# 🌐 GeoTracker-Python

A Python-based consent-based geolocation awareness dashboard designed for authorized development, testing, and educational purposes.

**Developer:** [negi748](https://github.com/negi748)  
**Repository:** [GeoTracker-Python](https://github.com/negi748/GeoTracker-Python)

---

## ✨ Features

- 🐍 Python-based web dashboard
- 🌐 Browser-based interface
- 📍 Consent-based location sharing
- 📷 Optional camera demonstration with explicit permission
- ☁️ Automatic Cloudflare Tunnel integration
- 🔗 Automatic temporary public HTTPS share link
- 📱 Termux (Android) support
- 🐧 Kali Linux support
- 💻 Local dashboard
- 🔐 Privacy-focused usage
- ⚡ Simple command-line startup

---

## 📋 Requirements

Before running the project, make sure you have:

- Python 3
- Git
- `cloudflared`
- Modern web browser
- Internet connection

`cloudflared` must be installed and available to the application for automatic public-link generation.

---

# 🚀 Quick Start

## 📱 Termux

Run the following command:

```bash
git clone https://github.com/negi748/GeoTracker-Python.git && cd GeoTracker-Python && (test -f requirements.txt && pip install -r requirements.txt || true) && python GPS.py
```

---

## 🐧 Kali Linux

Run:

```bash
git clone https://github.com/negi748/GeoTracker-Python.git && cd GeoTracker-Python && (test -f requirements.txt && pip3 install -r requirements.txt || true) && python3 GPS.py
```

---

# 🛠️ Manual Installation

## 1. Clone Repository

```bash
git clone https://github.com/negi748/GeoTracker-Python.git
```

## 2. Enter Project Directory

```bash
cd GeoTracker-Python
```

## 3. Install Requirements

### Python / Termux

```bash
pip install -r requirements.txt
```

### Kali Linux

```bash
pip3 install -r requirements.txt
```

## 4. Start the Application

### Python / Termux

```bash
python GPS.py
```

### Kali Linux

```bash
python3 GPS.py
```

---

# ☁️ Automatic Cloudflare Tunnel

GeoTracker-Python can automatically use Cloudflare Tunnel to create a temporary public HTTPS URL.

When the application starts, you may see something similar to:

```text
[INFO] Generating public link via Cloudflare Tunnel...
Press CTRL+C to stop...

PUBLIC SHARE LINK:
https://example-name.trycloudflare.com/share/...
```

No manual tunnel command is required when the automatic tunnel feature is available.

---

# 🔄 How It Works

**Run `GPS.py`**

↓  

**Python Web Server**

↓  

**Local Dashboard**

↓  

**Cloudflare Tunnel**

↓  

**Temporary HTTPS URL**

↓  

**PUBLIC SHARE LINK**

---

# 🌐 Dashboard

The application may provide a local dashboard such as:

```text
http://127.0.0.1:8765
```

A temporary public share link may look like:

```text
https://example-name.trycloudflare.com/share/...
```

Only share the generated public URL with people who have explicitly agreed to participate.

---

# 📱 Termux Installation

Update Termux packages:

```bash
pkg update
```

Install Python and Git:

```bash
pkg install python git
```

Clone the repository:

```bash
git clone https://github.com/negi748/GeoTracker-Python.git
```

Enter the project directory:

```bash
cd GeoTracker-Python
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python GPS.py
```

---

# 🐧 Kali Linux Installation

Update packages:

```bash
sudo apt update
```

Install required packages:

```bash
sudo apt install python3 python3-pip git
```

Clone the repository:

```bash
git clone https://github.com/negi748/GeoTracker-Python.git
```

Enter the project directory:

```bash
cd GeoTracker-Python
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

Start the application:

```bash
python3 GPS.py
```

---

# ☁️ Cloudflare Requirements

Check whether `cloudflared` is installed:

```bash
cloudflared --version
```

Official Cloudflare documentation:

https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/do-more-with-tunnels/trycloudflare/

---

# ⚠️ Public Tunnel Warning

A public Cloudflare Tunnel URL can make your local application temporarily accessible from the internet.

Use it responsibly.

- ❌ Do not expose private or sensitive services.
- ❌ Do not publish passwords or API keys.
- ❌ Do not share generated URLs unnecessarily.
- ❌ Do not expose personal information.
- ✅ Stop the application when you are finished.
- ✅ Use `CTRL + C` to stop the application.
- ✅ Only share the link with people who have given consent.

---

# 🔐 Privacy & Safety

GeoTracker-Python is intended for **consent-based** and authorized use.

Always:

- Get explicit consent before collecting location information.
- Explain what information is being collected.
- Collect only the information necessary for the intended purpose.
- Never secretly track people.
- Never secretly capture photos.
- Never attempt to bypass browser permission controls.
- Never publish private location information.
- Never commit passwords, API keys, or other secrets to GitHub.

---

# 🛡️ Security

Never publish sensitive information inside this repository.

Do not commit:

- API keys
- Passwords
- Authentication tokens
- Private location data
- Personal information
- Cloudflare credentials
- Private configuration files
- Session secrets

Use `.gitignore` to prevent sensitive files from being committed.

---

# 🔧 Troubleshooting

## Check Python

```bash
python --version
```

or:

```bash
python3 --version
```

## Check Git

```bash
git --version
```

## Check Cloudflared

```bash
cloudflared --version
```

## Check Project Files

```bash
ls
```

If the application does not start, verify that:

- Python 3 is installed.
- Dependencies are installed.
- `GPS.py` exists.
- `requirements.txt` is available when required.
- `cloudflared` is installed if public tunnel functionality is being used.
- Your browser allows the requested permissions.
- Your internet connection is working.

---

# 📁 Project Structure

```text
GeoTracker-Python/
├── GPS.py
├── README.md
├── .gitignore
└── requirements.txt
```

---

# 💻 Development

Clone the repository:

```bash
git clone https://github.com/negi748/GeoTracker-Python.git
```

Create a development environment if desired:

```bash
python -m venv venv
```

Activate it on Linux/Termux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python GPS.py
```

---

# 🤝 Contributing

Contributions, improvements, bug fixes, and educational suggestions are welcome.

Before submitting changes:

1. Test your changes locally.
2. Keep the project privacy-focused.
3. Do not add unauthorized tracking functionality.
4. Do not commit secrets or sensitive information.
5. Clearly describe your changes.

---

# 📄 License

This project is licensed under the MIT License.

Copyright © 2026 **negi748**

---

# 👨‍💻 Author

**negi748**

GitHub:  
https://github.com/negi748

Project:  
https://github.com/negi748/GeoTracker-Python

---

# ⚠️ Disclaimer

GeoTracker-Python is provided for **authorized development, testing, research, and educational purposes**.

Use this software only when you have appropriate permission and informed consent from the people whose information may be processed.

The developer is not responsible for misuse of this software or for unlawful tracking, surveillance, privacy violations, or unauthorized data collection.
