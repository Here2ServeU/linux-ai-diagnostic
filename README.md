# Linux AI Diagnostic Tool

This is an AI-powered Python tool that helps you **detect, mitigate, and predict** Linux OS issues such as high CPU usage, memory exhaustion, or disk pressure. It also provides **GPT-4 explanations** for faster root cause analysis.

---

## Project Structure

```bash
linux-ai-diagnostic/
├── detector.py             # Detects system issues
├── mitigator.py            # Suggests or automates mitigation
├── predictor.py            # Forecasts performance trends
├── main.py                 # Base CLI tool (without GPT)
├── main_with_gpt_support.py # Full CLI with GPT-4 analysis
├── requirements.txt        # Python dependencies
```

---

## What Each File Does

### `detector.py`
- Uses `psutil` and `shutil` to inspect:
  - CPU usage
  - Memory usage
  - Disk usage
- Returns a list of active issues (e.g., "High memory usage: 91%").

---

### `mitigator.py`
- Analyzes current system issues.
- Suggests mitigation steps:
  - Kill or inspect top resource-intensive processes.
  - Clean up `/tmp` or old logs using `journalctl`.

---

### `predictor.py`
- Generates dummy metrics for prediction (real metrics can be plugged in).
- Performs simple trend analysis on CPU/memory using `pandas`.
- Flags when usage is likely to become critical soon.

---

### `main.py`
- CLI entry point (no GPT).
- Runs detection, mitigation, and prediction.
- Useful if you want a lightweight version of the tool without OpenAI integration.

---

### `main_with_gpt_support.py`
- Same as `main.py`, **plus GPT-4 integration**.
- Takes detected issues and mitigation suggestions, then summarizes them with AI using the OpenAI API.
- Requires your `OPENAI_API_KEY`.

---

### `requirements.txt`
Contains the Python packages required:
```text
psutil
pandas
openai
python-dotenv
```

Install them with:
```bash
pip install -r requirements.txt
```

---

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Here2ServeU/linux-ai-diagnostic.git
cd linux-ai-diagnostic
```

---

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 3. (Optional) Setup OpenAI API Key

If using GPT support:
```bash
echo "OPENAI_API_KEY=your_openai_key_here" > .env
```

Or export it in your terminal session:
```bash
export OPENAI_API_KEY=your_openai_key_here
```

---

### 4. Run the Tool

#### 🔹 Without GPT:
```bash
python3 main.py
```

#### 🔹 With GPT-4 Analysis:
```bash
python3 main_with_gpt_support.py
```

---

## Example Output

```bash
**Running Linux AI Diagnostic...**

**Issues detected**:
- High CPU usage detected: 93.2%
- High memory usage: 88%

**Mitigation suggestions**:
- Top resource processes:
  PID  CMD      %CPU
  1234 nginx     67.1%
  4321 java      22.0%
- Try clearing /tmp or log files via: sudo journalctl --vacuum-time=3d

**GPT Explanation**:
High CPU usage is likely due to background services consuming excessive compute power. Consider restarting the service or analyzing logs under `/var/log`.

**Predictive Analysis**:
Memory usage trend is approaching danger zone.
```

---

## Security Note

This tool **does not perform any automatic destructive actions** (e.g., killing processes or deleting files). All mitigation steps are suggestions only.

---

## Author

**Dr. Emmanuel Naweji**  
Cloud | DevOps | SRE | FinOps | AI Engineer  
GitHub: [Here2ServeU](https://github.com/Here2ServeU)

---

## License

MIT License — feel free to use, modify, and distribute.
