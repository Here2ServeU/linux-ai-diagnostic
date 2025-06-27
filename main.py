from detector import detect_issues
from mitigator import mitigate
from predictor import generate_dummy_metrics, predict_trend

def main():
    print("🔍 Running Linux AI Diagnostic...\n")
    
    issues = detect_issues()
    if issues:
        print("Issues detected:")
        for issue in issues:
            print(f"- {issue}")

        print("\n🛠 Mitigation suggestions:")
        for fix in mitigate(issues):
            print(f"- {fix}")
    else:
        print("No critical issues detected.")

    print("\n Predictive Analysis:")
    df = generate_dummy_metrics()
    print(predict_trend(df))

if __name__ == "__main__":
    main()
