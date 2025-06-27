from detector import detect_issues
from mitigator import mitigate
from predictor import generate_dummy_metrics, predict_trend
from openai import OpenAI
import os

# GPT-based root cause explanation
api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(summary):
    if not api_key:
        return "OPENAI_API_KEY not found in environment. GPT explanation skipped."
    
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
        return f"GPT call failed: {str(e)}"

def main():
    print("Running Linux AI Diagnostic...\n")

    issues = detect_issues()
    if issues:
        print("Issues detected:")
        for issue in issues:
            print(f"- {issue}")
        
        print("\n Mitigation suggestions:")
        mitigations = mitigate(issues)
        for fix in mitigations:
            print(f"- {fix}")

        # GPT Explanation
        print("\n GPT Explanation:")
        issue_summary = "\n".join(issues + mitigations)
        gpt_response = ask_gpt(issue_summary)
        print(gpt_response)
    else:
        print("No critical issues detected.")

    print("\n Predictive Analysis:")
    df = generate_dummy_metrics()
    print(predict_trend(df))

if __name__ == "__main__":
    main()
