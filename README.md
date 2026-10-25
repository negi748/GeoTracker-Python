# GeoTracker-Python

A Python-based geolocation awareness dashboard.

## Features

- Python-based dashboard
- Browser-based interface
- Consent-based location sharing
- Optional camera demo with explicit permission
- Termux (Android) support
- Kali Linux support
- Optional Cloudflare Tunnel integration

## Requirements

- Python 3
- Git
- Compatible web browser

## Installation

Clone the repository:

    git clone https://github.com/negi748/GeoTracker-Python.git
    cd GeoTracker-Python

Install dependencies if requirements.txt exists:

    python -m pip install -r requirements.txt

Run the application using the command documented for the project.

## Privacy and Safety

- Obtain explicit consent before collecting location or photos.
- Clearly explain what information is collected.
- Never track people or capture their photos without their knowledge and consent.
- Never publish API keys, passwords, access tokens, or private user data.

## Platforms

Installation instructions are intended for Android Termux and Kali Linux.
Actual dependencies and run commands depend on the project implementation.

## License

MIT

## Cloudflare Tunnel (Temporary Public URL)

Cloudflare Quick Tunnels are intended for development and testing.
They expose a local HTTP service through a temporary public HTTPS URL.

Official documentation:
https://developers.cloudflare.com/tunnel/get-started/quick-tunnels/

### How it works

1. Start the Python application on localhost.
2. Identify the local port used by the application.
3. Install cloudflared for your operating system.
4. Start a Quick Tunnel pointing to the local application.
5. Open the generated trycloudflare.com URL in your browser.
6. Stop the tunnel with Ctrl+C when testing is complete.

### Important notes

- The local application must be running before starting the tunnel.
- Use the actual port configured in your Python application.
- The generated URL is temporary and changes between sessions.
- Anyone with the public URL may be able to access the exposed application.
- Do not expose private dashboards or sensitive information.
- Obtain informed consent before collecting location or camera data.
- Never publish Cloudflare credentials, tunnel tokens, or private user data.
- Quick Tunnels are for development and testing, not production hosting.

### Termux and Kali Linux

Installation instructions depend on the device architecture and
operating system. Consult the official Cloudflare downloads page:

https://developers.cloudflare.com/tunnel/downloads/

After installation, verify the command is available:

    cloudflared --version

For a local test application listening on port 8080, the general
Quick Tunnel command is:

    cloudflared tunnel --url http://localhost:8080

Replace port 8080 with the actual port of your own test application.

### Stop the tunnel

Press Ctrl+C in the terminal running cloudflared.
The temporary public URL will stop working when the tunnel process ends.
