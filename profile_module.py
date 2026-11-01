
def collect_profile():
    print("\n--- PATIENT PROFILE ---")

    return {
        "Age": input("Age: ").strip() or "Not provided",
        "Sex": input("Sex (optional): ").strip() or "Not provided",
        "Duration": input("Duration of symptoms: ").strip() or "Not provided",
        "Severity": input("Severity (mild/moderate/severe): ").strip() or "Not provided",
        "Medical History": input("Medical history: ").strip() or "Not provided",
        "Medications": input("Current medications: ").strip() or "Not provided",
        "Allergies": input("Allergies: ").strip() or "Not provided"
    }
