# AI-Powered Linux Diagnostic Assistant with Chaos Simulation and Alerts

## Overview

This project provides a CLI tool that uses Python and optional GPT-4 support to:
- Detect high CPU, memory, and disk usage
- Suggest mitigation steps
- Predict performance risks
- Trigger alerts via **Slack** and **Email**
- Simulate **chaos scenarios** (e.g., high memory or CPU usage) for testing

---

## Challenge (Context)

Troubleshooting performance issues on Linux can be manual and time-consuming. Engineers often lack fast, explainable diagnostics or proactive alerts. This tool bridges that gap with built-in AI and automation logic.

---

## Objective

To provide a DevOps/SRE-friendly tool that:
- Detects real-time issues
- Predicts failure patterns
- Explains root causes using GPT
- Sends alerts via Slack and Email
- Simulates chaos scenarios for testing monitoring setups

---

## Project Structure

```
linux-ai-diagnostic/
├── detector.py               # Detect issues using psutil
├── mitigator.py              # Suggest fixes
├── predictor.py              # Forecast risk trends
├── notifier.py               # Email + Slack alerts
├── chaos_simulator.py        # Generate high CPU/memory load
├── main.py                   # Basic CLI
├── main_with_gpt_support.py  # With GPT explanation
├── main_with_alerts.py       # With alerting support
├── requirements.txt
├── .env                      # Store secrets securely
├── .gitignore                # Prevent secrets from being committed
```

---

## Setup Guide

### 1. EC2 Prerequisites

```bash
sudo apt update && sudo apt install -y git python3 python3-pip python3-venv
```

### 2. Clone and Install

```bash
git clone https://github.com/Here2ServeU/linux-ai-diagnostic.git
cd linux-ai-diagnostic
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. (Optional) Add OpenAI Key

```bash
echo "OPENAI_API_KEY=your_key_here" > .env
```

### 4. Add Slack and Email Secrets

Add the following to your `.env` file:

```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/XXX/YYY/ZZZ
```

> ⚠️ Don't forget to secure `.env` using `.gitignore` (already included in this repo).

---

## Running the Tool

### Without GPT

```bash
python3 main.py
```

### With GPT Support

```bash
python3 main_with_gpt_support.py
```

### With GPT + Slack + Email Alerts

```bash
python3 main_with_alerts.py
```

---

## Simulate Chaos (for Testing)

### Trigger High Memory Usage

```bash
python3 chaos_simulator.py --memory 80
```

### Trigger High CPU Usage

```bash
python3 chaos_simulator.py --cpu 4
```

This runs dummy workloads to cross alert thresholds.

---

## Slack and Email Integration (Step-by-Step)

### 1. Slack Setup

- Go to: https://api.slack.com/apps
- Create a new app → Incoming Webhooks → Enable
- Add to workspace and copy the **Webhook URL**
- Paste it into `.env` under `SLACK_WEBHOOK_URL`

### 2. Gmail Email Setup

- Use Gmail App Passwords (https://myaccount.google.com/apppasswords)
- In `.env`, add:

```
EMAIL_ADDRESS=youremail@gmail.com
EMAIL_PASSWORD=your_app_password
```

---

## Sample Output

```bash
Issues Detected:
- High CPU usage detected: 92%
- High memory usage: 86%

Suggestions:
- Review top CPU-intensive processes
- Clear /tmp files and compress logs

GPT Summary:
High resource usage due to a Java process. Recommend inspecting logs in /var/log/java.

Notification sent:
- Email alert
- Slack alert
```

---

## Safe Defaults

- This tool only **detects and notifies**
- It does **not kill or delete anything** automatically

---

## Author

By Emmanuel Naweji, 2025  
**Cloud | DevOps | SRE | FinOps | AI Engineer**  

Helping businesses modernize infrastructure and guiding engineers into top 1% career paths through real-world projects and automation-first thinking.

![AWS Certified](https://img.shields.io/badge/AWS-Certified-blue?logo=amazonaws)
![Azure Solutions Architect](https://img.shields.io/badge/Azure-Solutions%20Architect-0078D4?logo=microsoftazure)
![CKA](https://img.shields.io/badge/Kubernetes-CKA-blue?logo=kubernetes)
![Terraform](https://img.shields.io/badge/IaC-Terraform-623CE4?logo=terraform)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-blue?logo=githubactions)
![GitLab CI](https://img.shields.io/badge/CI/CD-GitLab%20CI-FC6D26?logo=gitlab)
![Jenkins](https://img.shields.io/badge/CI/CD-Jenkins-D24939?logo=jenkins)
![Ansible](https://img.shields.io/badge/Automation-Ansible-red?logo=ansible)
![ArgoCD](https://img.shields.io/badge/GitOps-ArgoCD-orange?logo=argo)
![VMware](https://img.shields.io/badge/Virtualization-VMware-607078?logo=vmware)
![Linux](https://img.shields.io/badge/OS-Linux-black?logo=linux)
![FinOps](https://img.shields.io/badge/FinOps-Cost%20Optimization-green?logo=money)
![OpenAI](https://img.shields.io/badge/AI-OpenAI-ff9900?logo=openai)

---

## Connect with Me

- [LinkedIn](https://www.linkedin.com/in/ready2assist/)
- [GitHub](https://github.com/Here2ServeU)
- [Medium](https://medium.com/@here2serveyou)

---

## Book a Free Consultation

Ready to adopt GitOps or scale your Kubernetes infrastructure?  
[Schedule a free 1:1 consultation](https://bit.ly/letus-meet)

