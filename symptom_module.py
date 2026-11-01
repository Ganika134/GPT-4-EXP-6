
import ollama

MODEL = "llama3.2"


def extract_symptoms(text):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Extract only symptoms explicitly reported by the user. "
                    "Do not invent symptoms. Return a concise bullet list."
                )
            },
            {"role": "user", "content": text}
        ],
        options={"temperature": 0}
    )

    return response["message"]["content"]
