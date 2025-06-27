import psutil
import shutil

def detect_issues():
    issues = []

    # CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > 80:
        issues.append(f"High CPU usage detected: {cpu_usage}%")

    # Memory
    mem = psutil.virtual_memory()
    if mem.percent > 80:
        issues.append(f"High memory usage: {mem.percent}%")

    # Disk
    total, used, free = shutil.disk_usage("/")
    if used / total * 100 > 90:
        issues.append(f"Disk space critically low: {(used/total)*100:.2f}% used")

    return issues
