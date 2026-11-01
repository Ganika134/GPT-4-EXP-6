
import ollama

MODEL = "llama3.2"


def analyze(prompt):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Provide cautious, understandable health information. "
                    "Never claim certainty or diagnose a patient."
                )
            },
            {"role": "user", "content": prompt}
        ],
        options={"temperature": 0.2}
    )

    return response["message"]["content"]
