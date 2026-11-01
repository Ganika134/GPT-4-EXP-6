
import ollama

MODEL = "llama3.2"


def find_missing_information(profile, symptoms):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Identify relevant missing information for an "
                    "educational symptom assessment. Consider duration, "
                    "severity, associated symptoms and warning signs. "
                    "Do not invent patient facts. Use bullet points."
                )
            },
            {
                "role": "user",
                "content": f"Profile: {profile}\nSymptoms: {symptoms}"
            }
        ],
        options={"temperature": 0}
    )

    return response["message"]["content"]
