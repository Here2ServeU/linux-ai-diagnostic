import smtplib
from email.message import EmailMessage
import requests

def send_email(subject, body, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = "your_email@example.com"
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("your_email@example.com", "your_app_password")
        smtp.send_message(msg)

def send_slack_alert(message, webhook_url):
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    return response.status_code
