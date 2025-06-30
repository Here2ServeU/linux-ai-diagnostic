from detector import detect_issues
from mitigator import mitigate
from predictor import generate_dummy_metrics, predict_trend
from openai import OpenAI
from notifier import send_email, send_slack_alert
import os

api_key = os.getenv("OPENAI_API_KEY")

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
        body = "\n".join(issues)
        send_email("Linux AI Alert", body, "your_email@example.com")
        send_slack_alert(f"Linux AI Alert:\n{body}", "your_slack_webhook_url")
    else:
        print("No critical issues detected.")

    print("\nPredictive Analysis:")
    df = generate_dummy_metrics()
    print(predict_trend(df))

if __name__ == "__main__":
    main()
