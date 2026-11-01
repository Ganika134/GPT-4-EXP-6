
def get_symptoms():
    print("\n--- SYMPTOM INPUT ---")
    symptoms = input("Describe your symptoms: ").strip()

    while not symptoms:
        print("Symptoms cannot be empty.")
        symptoms = input("Describe your symptoms: ").strip()

    return symptoms
