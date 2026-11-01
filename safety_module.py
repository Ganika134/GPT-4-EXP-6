
def get_safety_guidance(text):
    text = text.lower()

    warning_signs = [
        "chest pain",
        "difficulty breathing",
        "can't breathe",
        "cannot breathe",
        "severe bleeding",
        "unconscious",
        "stroke symptoms"
    ]

    if any(sign in text for sign in warning_signs):
        return (
            "URGENT SAFETY NOTICE:\n"
            "A reported symptom may require urgent assessment. "
            "Seek immediate professional emergency care if it is "
            "happening now. Do not wait for an AI response."
        )

    return (
        "MEDICAL ATTENTION GUIDANCE:\n"
        "Seek professional medical advice if symptoms persist, "
        "worsen, or cause concern. Seek emergency care for severe "
        "or potentially life-threatening symptoms. This application "
        "does not make clinical triage decisions."
    )
