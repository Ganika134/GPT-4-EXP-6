
from input_module import get_symptoms
from profile_module import collect_profile
from symptom_module import extract_symptoms
from context_module import find_missing_information
from prompt_module import build_prompt, DISCLAIMER
from analysis_module import analyze
from question_module import generate_questions
from safety_module import get_safety_guidance
from save_module import save_report
from utils import print_heading, format_profile


def main():
    profile = {}
    symptoms = ""
    report = ""

    while True:
        print_heading("MEDICAL SYMPTOM ASSISTANT - OLLAMA")
        print("1. Enter Patient Information")
        print("2. Enter Symptoms")
        print("3. Analyze Symptoms")
        print("4. Generate Follow-up Questions")
        print("5. Display Possible Conditions")
        print("6. Display Medical Attention Guidance")
        print("7. Display Disclaimer")
        print("8. Save Report")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        try:
            # Option 1: Patient information
            if choice == "1":
                profile = collect_profile()

            # Option 2: Symptom input
            elif choice == "2":
                symptoms = get_symptoms()

            # Option 3: Complete symptom analysis
            elif choice == "3":
                if not profile or not symptoms:
                    print(
                        "Enter patient information and symptoms first."
                    )
                    continue

                print("\nExtracting symptoms...")
                extracted = extract_symptoms(symptoms)
                print("\n--- EXTRACTED SYMPTOMS ---")
                print(extracted)

                print("\nChecking missing information...")
                missing = find_missing_information(
                    profile, symptoms
                )
                print("\n--- CONTEXT ANALYSIS ---")
                print(missing)

                # Generate the prompt
                prompt = build_prompt(
                    profile, symptoms, extracted, missing
                )

                # Display prompt for Screenshot 6
                print_heading("PROMPT GENERATION - OLLAMA")
                print("The following prompt will be sent to Ollama:\n")
                print("-" * 60)
                print(prompt)
                print("-" * 60)

                # Send prompt to Ollama
                print("\nAnalyzing with Ollama...")
                analysis = analyze(prompt)

                # Generate safety guidance
                safety = get_safety_guidance(
                    symptoms + " " + format_profile(profile)
                )

                # Build complete report
                report = (
                    "AI-POWERED MEDICAL SYMPTOM ASSISTANT\n\n"
                    "1. PATIENT INFORMATION\n"
                    + format_profile(profile)
                    + "\n\n2. REPORTED SYMPTOMS\n"
                    + extracted
                    + "\n\n3. CONTEXT ANALYSIS\n"
                    + missing
                    + "\n\n4. OLLAMA LLM RESPONSE\n"
                    + analysis
                    + "\n\n5. MEDICAL ATTENTION GUIDANCE\n"
                    + safety
                    + "\n\n6. DISCLAIMER\n"
                    + DISCLAIMER
                )

                print_heading("COMPLETE STRUCTURED ANALYSIS")
                print(report)

            # Option 4: Follow-up questions
            elif choice == "4":
                if not symptoms:
                    print("Enter symptoms first.")
                    continue

                questions = generate_questions(
                    profile, symptoms
                )

                print_heading("FOLLOW-UP QUESTIONS")
                print(questions)

                if report:
                    report += (
                        "\n\nFOLLOW-UP QUESTIONS\n" + questions
                    )

            # Option 5: Possible conditions
            elif choice == "5":
                if not report:
                    print("Analyze symptoms first.")
                    continue

                print_heading("POSSIBLE CONDITIONS")

                start = report.lower().find(
                    "3. possible conditions"
                )

                if start != -1:
                    end = report.find("\n4.", start)
                    print(
                        report[start:end if end != -1 else None]
                    )
                else:
                    print(
                        "Review the POSSIBLE CONDITIONS section "
                        "in the Ollama LLM response above."
                    )

            # Option 6: Medical attention guidance
            elif choice == "6":
                safety = get_safety_guidance(
                    symptoms + " " + format_profile(profile)
                )

                print_heading("MEDICAL ATTENTION GUIDANCE")
                print(safety)

            # Option 7: Disclaimer
            elif choice == "7":
                print_heading("MEDICAL DISCLAIMER")
                print(DISCLAIMER)

            # Option 8: Save report
            elif choice == "8":
                if report:
                    save_report(report)
                else:
                    print("Analyze symptoms before saving.")

            # Option 9: Exit
            elif choice == "9":
                print("Exiting Medical Symptom Assistant.")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 9.")

        except Exception as error:
            print("\nAn error occurred:", error)
            print(
                "Check that Ollama is running and the model "
                "is installed. Run: ollama list"
            )


if __name__ == "__main__":
    main()
