import speech_recognition as sr

def human_edit(input_file='chapter1_reviewed.txt', output_file='chapter1_final.txt'):
    print("\nLoading reviewed chapter...\n")
    with open(input_file, 'r', encoding='utf-8') as f:
        reviewed_text = f.read()

    print("Preview:\n")
    print(reviewed_text[:500], "...\n")

    choice = input("Would you like to edit manually by typing or by voice? (type/voice): ").strip().lower()

    if choice == "voice":
        print("Speak your edited version. Say 'stop recording' to end.")
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, phrase_time_limit=30)

        try:
            text = recognizer.recognize_google(audio)
            print(f"Transcribed:\n{text}")
            edited_text = text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return
        except sr.RequestError:
            print("Could not request results; check your internet.")
            return
    else:
        print("Now you can enter your own edits.")
        print("Type your edited version below. To finish, enter a single line with `--END--`.\n")
        lines = []
        while True:
            line = input()
            if line.strip() == "--END--":
                break
            lines.append(line)
        edited_text = "\n".join(lines)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(edited_text)
    print(f"Manual edits captured and saved.\nFinal version saved as: {output_file}")
