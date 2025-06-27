import os
import subprocess

def mitigate(issues):
    responses = []
    for issue in issues:
        if "CPU" in issue or "memory" in issue:
            # Suggest restarting heavy processes
            output = subprocess.getoutput("ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -n 10")
            responses.append(f"Top resource processes:\n{output}")
        if "Disk" in issue:
            responses.append("Try clearing /tmp or log files via: sudo journalctl --vacuum-time=3d")
    return responses
