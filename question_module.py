
import ollama

MODEL = "llama3.2"


def generate_questions(profile, symptoms):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Generate 5 concise follow-up questions for an "
                    "educational symptom assessment. Ask about relevant "
                    "severity, duration, associated symptoms and warning "
                    "signs. Do not diagnose or prescribe."
                )
            },
            {
                "role": "user",
                "content": f"Profile: {profile}\nSymptoms: {symptoms}"
            }
        ],
        options={"temperature": 0.2}
    )

    return response["message"]["content"]
