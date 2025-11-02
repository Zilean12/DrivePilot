# DrivePilot

![GitHub stars](https://img.shields.io/github/stars/Zilean12/DrivePilot?style=social)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

A friendly, lightweight toolkit to integrate Python with Google Drive — upload, download, update files, and manage folders programmatically with clear examples and helpful utilities. 🚀

> Star the repo to stay updated and motivate development!

---

## Table of Contents
- [Project Overview](#project-overview)
- [Why DrivePilot?](#why-drivepilot)
- [Features](#features)
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
---

## Project Overview

DrivePilot provides simple, reusable Python scripts and helpers to interact with the Google Drive API. It's ideal for automating backups, synchronizing assets, or building tooling that needs programmatic access to Drive.

<!-- Optional: Add a banner or GIF demo here
![DrivePilot Demo](docs/images/demo.gif)
-->

## Why DrivePilot?

- 🧩 Minimal setup, friendly code
- ⚡ Fast start with copy-paste examples
- 🧰 Covers common Drive tasks (upload, download, update, organize)
- 🧭 Clear, documented workflows and tips

## Features

- ✅ Easy file upload and download
- ♻️ Update and overwrite files on Drive
- 🗂️ Create and manage folders
- 🏷️ Support for custom layouts and metadata
- 📄 Minimal, well-documented Python code

## Requirements

- Python 3.8+
- A Google Cloud project with the Google Drive API enabled
- OAuth 2.0 Client Credentials or a Service Account (for server-to-server)

## Quick Start

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create (or select) a project
3. Enable the "Google Drive API"
4. Create credentials:
   - For desktop/scripts: OAuth Client ID (type: Desktop App)
   - For backend/server: Service Account
5. Download your credentials (credentials.json or service account JSON)

## Installation

```bash
git clone https://github.com/Zilean12/DrivePilot.git
cd DrivePilot
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

- Place your OAuth credentials file (credentials.json) in the project root
- For Service Accounts, store your JSON key securely and set an environment variable pointing to it

Example .env (optional):

```env
GOOGLE_APPLICATION_CREDENTIALS=path/to/service_account.json
DRIVEPILOT_SCOPES=https://www.googleapis.com/auth/drive
```

> Tip: Keep credentials out of version control. Use .gitignore.

## Usage Examples

Upload a file (example):

```python
from drivepilot import uploader

uploader.upload_file('path/to/local/file.txt', "My Drive Folder/Subfolder")
```

Download a file (example):

```python
from drivepilot import downloader

downloader.download_file('drive-file-id', 'path/to/save/file.txt')
```

Create a folder (example):

```python
from drivepilot import folders

folders.create_folder('Project Assets/2025')
```

List files in a folder (example):

```python
from drivepilot import explorer

files = explorer.list_files('My Drive Folder/Subfolder')
for f in files:
    print(f['name'], f['id'])
```

> For more complete examples and advanced usage, explore the scripts in the `examples/` directory.

## Troubleshooting

- auth_error: Make sure credentials.json exists and matches your OAuth client.
- insufficientPermissions: Ensure the scope includes `https://www.googleapis.com/auth/drive`.
- fileNotFound: Verify the Drive file ID or path and permissions (shared drive vs my drive).

## Roadmap

- [ ] Add progress bars for uploads/downloads
- [ ] Add sync (local ↔ Drive) utility
- [ ] Add CLI wrapper (drivepilot) for common tasks
- [ ] Add docs site with more samples and gifs

## Contributing

Contributions, issues and feature requests are welcome! Please open an issue or submit a pull request. To contribute:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'feat: add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request
---

If this project helps you, consider giving it a ⭐!
