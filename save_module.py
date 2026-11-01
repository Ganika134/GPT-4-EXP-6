
import os
from datetime import datetime


def save_report(report):
    os.makedirs("outputs", exist_ok=True)

    with open(
        "outputs/medical_analysis.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write("AI-POWERED MEDICAL SYMPTOM ASSISTANT\n")
        file.write(f"Generated: {datetime.now()}\n\n")
        file.write(report)

    print("\nReport saved to outputs/medical_analysis.txt")
