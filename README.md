# Case Study: AI-Powered Linux Diagnostic Assistant

## Challenge Encountered (Context)

Troubleshooting performance issues on Linux—such as high CPU usage, memory saturation, or disk bottlenecks—is often a complex and manual task. System administrators typically rely on command-line tools, scripts, and tribal knowledge to understand what's wrong and how to resolve it. This reactive approach increases downtime risk and demands significant expertise.

## Goal Set (Objective)

The objective was to create an intelligent, developer-friendly CLI tool that:
- Automatically detects common Linux system issues in real-time
- Recommends actionable mitigation steps
- Predicts performance trends using system metrics
- Uses GPT-4 for human-readable explanations and summaries

## Work Done (Implementation)

A modular Python application was developed with both local and GPT-powered logic:

### Project Structure

```
linux-ai-diagnostic/
├── detector.py               # Detect current system issues
├── mitigator.py              # Recommend mitigations
├── predictor.py              # Forecast performance problems
├── main.py                   # CLI version without GPT
├── main_with_gpt_support.py  # GPT-4 enhanced CLI
├── requirements.txt          # Python dependencies
```

### Key Components

- **detector.py** – Identifies CPU, memory, and disk issues using `psutil`
- **mitigator.py** – Suggests fixes such as cleaning `/tmp` or restarting services
- **predictor.py** – Generates dummy or real metrics to forecast risk zones
- **main.py** – CLI without GPT
- **main_with_gpt_support.py** – Adds OpenAI integration for explanation of issues

### Installation Instructions

**Debian/Ubuntu**
```
sudo apt update
sudo apt install -y python3 python3-pip
```

**RHEL/CentOS**
```
sudo yum install -y python3 python3-pip
```

**(Recommended) Create a Virtual Environment**
```
python3 -m venv venv
source venv/bin/activate
```

**Setup**
```
git clone https://github.com/Here2ServeU/linux-ai-diagnostic.git
cd linux-ai-diagnostic
pip install -r requirements.txt
```

**(Optional) Set up OpenAI API**
```
echo "OPENAI_API_KEY=your_key_here" > .env
```

### Running the Tool

**Without GPT**
```
python3 main.py
```

**With GPT-4 Support**
```
python3 main_with_gpt_support.py
```

## Impact Observed (Results)

Sample Output:
```
Issues Detected:
- High CPU usage detected: 93.2%
- High memory usage: 88%

Mitigation Recommendations:
- Top resource-intensive processes listed
- Suggest cleanup: sudo journalctl --vacuum-time=3d

GPT Summary:
High CPU usage is likely due to background services consuming excess resources.

Forecast:
Memory usage trend is approaching a critical threshold.
```

The tool helped administrators reduce time spent identifying and reacting to issues, while also enabling predictive awareness and AI-guided summaries.

## Safeguards (Limitations)

No destructive actions are taken automatically. All recommendations are non-invasive and designed to be reviewed by a human before applying.

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
👉🏾 [Schedule a free 1:1 consultation](https://bit.ly/letus-meet)
