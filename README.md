# 🛡️ CloudShield - Zero-Trust Access Control Platform

<div align="center">
  
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)](https://python.org)
[![AWS](https://img.shields.io/badge/AWS-S3-orange?style=for-the-badge&logo=amazon-aws)](https://aws.amazon.com/s3/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

## 📋 Overview

**CloudShield** is a zero-trust access control platform for AWS S3 that automates IAM policy management and bucket security. Built for security automation engineers.

### ✨ Features

| Feature | Description |
|---------|-------------|
| 🔐 **IAM Policy Automation** | Create, validate, and attach IAM policies |
| 📦 **S3 Bucket Management** | List, create, and configure buckets |
| 🎯 **Least Privilege** | Apply read-only/write-only policies |
| 📊 **Access Analyzer** | Validate policies before deployment |
| 🖥️ **Streamlit UI** | Easy-to-use web interface |

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/salhabheba-cyber/CloudShield.git
cd CloudShield

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Configure AWS credentials
cp .env.example .env
# Edit .env with your AWS keys

# Run the application
streamlit run src/app.py
User → Streamlit UI → Python Backend → AWS API
                                        ├── IAM
                                        ├── S3
                                        └── Access Analyzer

🔒 Security Best Practices
✅ No public bucket access by default

✅ Least privilege IAM policies

✅ Policy validation before deployment

✅ MFA enforcement ready

CloudShield/
├── src/
│   ├── app.py           # Streamlit UI
│   ├── iam_manager.py   # IAM policy management
│   └── s3_manager.py    # S3 bucket management
├── screenshots/          # Documentation images
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
├── .gitignore           # Git ignore file
├── LICENSE              # MIT License
└── README.md            # This file

👩‍💻 Author
Heba Salhab

📍 Beirut, Lebanon

🐙 GitHub: @salhabheba-cyber

🔗 LinkedIn: Hiba Salhab

📄 License
MIT License - See LICENSE file for details.

<div align="center">
🛡️ CloudShield - Know the truth before you grant access

</div> ```
