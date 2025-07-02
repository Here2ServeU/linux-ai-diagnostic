import os
from dotenv import load_dotenv
from detector import detect_issues
from mitigator import mitigate
from predictor import generate_dummy_metrics, predict_trend
from notifier import send_email, send_slack_alert
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get secrets
api_key = os.getenv("OPENAI_API_KEY")
email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")
slack_webhook = os.getenv("SLACK_WEBHOOK_URL")

def ask_gpt(summary):
    if not api_key:
        return "OPENAI_API_KEY not found."
    client = OpenAI(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You're a Linux troubleshooting assistant."},
                {"role": "user", "content": summary}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"GPT error: {str(e)}"

def main():
    print("Running Linux AI Diagnostic...\n")
    issues = detect_issues()
    
    if issues:
        print("Issues Detected:")
        for issue in issues:
            print(f"- {issue}")

        print("\nMitigation Suggestions:")
        mitigations = mitigate(issues)
        for fix in mitigations:
            print(f"- {fix}")

        print("\nGPT Explanation:")
        summary = "\n".join(issues + mitigations)
        print(ask_gpt(summary))

        # Send alerts
        alert_body = "\n".join(issues + mitigations)
        send_email("Linux AI Alert", alert_body, email_address, email_address, email_password)
        send_slack_alert(alert_body, slack_webhook)
    else:
        print("No critical issues detected.")

    print("\nPredictive Analysis:")
    df = generate_dummy_metrics()
    print(predict_trend(df))

if __name__ == "__main__":
    main()
