
DISCLAIMER = """
This AI-generated response is for educational and informational
purposes only. It is not a medical diagnosis and does not replace
advice from a qualified healthcare professional. Seek appropriate
medical care for serious, worsening or urgent symptoms.
"""


def build_prompt(profile, raw_symptoms, extracted, missing):
    return f"""
You are an educational medical symptom information assistant.

PATIENT INFORMATION:
{profile}

USER'S DESCRIPTION:
{raw_symptoms}

EXTRACTED SYMPTOMS:
{extracted}

POTENTIALLY MISSING INFORMATION:
{missing}

Generate a report containing these sections:

1. Reported Symptoms
2. Patient Information
3. Possible Conditions
4. Explanation
5. Missing Information
6. Follow-up Questions
7. Medical Attention Guidance
8. Disclaimer

Rules:
- Discuss possible explanations, not a definitive diagnosis.
- Do not invent facts, test results or patient history.
- Do not prescribe medication or dosage.
- Explain uncertainty in simple language.
- Recommend professional medical assessment when appropriate.
- Do not claim to make a clinical triage decision.
- If emergency warning signs are reported, advise immediate
  professional emergency assessment.
- Include this disclaimer:

{DISCLAIMER}
"""
