# DrivePilot

![GitHub stars](https://img.shields.io/github/stars/Zilean12/DrivePilot?style=social)
![GitHub license](https://img.shields.io/github/license/Zilean12/DrivePilot)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

A friendly, lightweight toolkit to integrate Python with Google Drive — upload, download, update files, and manage folders programmatically with clear examples and helpful utilities.

---

Table of Contents
- Project Overview
- Features
- Quick Start
- Installation
- Configuration
- Usage Examples
- Contributing
- License

---

Project Overview

DrivePilot provides simple, reusable Python scripts and helpers to interact with the Google Drive API. It's ideal for automating backups, synchronizing assets, or building tooling that needs programmatic access to Drive.

Features

- Easy file upload and download
- Update and overwrite files on Drive
- Create and manage folders
- Support for custom layouts and metadata
- Minimal, well-documented Python code

Quick Start

1. Enable the Google Drive API in the Google Cloud Console and create credentials (OAuth 2.0 Client ID or Service Account) as needed.
2. Clone this repository.

Installation

```bash
git clone https://github.com/Zilean12/DrivePilot.git
cd DrivePilot
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Configuration

- Place your OAuth credentials (credentials.json) in the project root or configure environment variables for service account usage.
- See the examples/ directory for sample configuration files and usage patterns.

Usage Examples

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

For more complete examples and advanced usage, explore the scripts in the examples/ directory.

Contributing

Contributions, issues and feature requests are welcome! Please open an issue or submit a pull request. To contribute:

1. Fork the project
2. Create your feature branch (git checkout -b feature/YourFeature)
3. Commit your changes (git commit -m 'Add some feature')
4. Push to the branch (git push origin feature/YourFeature)
5. Open a Pull Request

License

This project is licensed under the MIT License — see the LICENSE file for details.

---
