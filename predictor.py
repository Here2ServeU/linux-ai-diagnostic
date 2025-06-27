import pandas as pd
import datetime
import random

def generate_dummy_metrics():
    now = datetime.datetime.now()
    data = {
        "timestamp": [now - datetime.timedelta(minutes=i) for i in range(60)],
        "cpu": [random.uniform(10, 80) for _ in range(60)],
        "memory": [random.uniform(30, 90) for _ in range(60)]
    }
    return pd.DataFrame(data)

def predict_trend(df):
    trend = df.tail(10).mean()
    if trend["cpu"] > 75:
        return "CPU usage trend is rising and may cross critical limit soon."
    if trend["memory"] > 80:
        return "Memory usage trend is approaching danger zone."
    return "System performance is within healthy limits."
