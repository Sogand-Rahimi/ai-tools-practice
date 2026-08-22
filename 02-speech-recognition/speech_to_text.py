# speech_to_text.py
# Speech to Text using audio file or microphone input

import speech_recognition as sr


def recognize_from_file(filename, language="en-US"):
    """Recognize speech from a local .wav audio file."""
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(filename) as source:
            print(f"Processing audio file '{filename}'...")
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio, language=language)
        return text

    except FileNotFoundError:
        return f"Error: File '{filename}' was not found."
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"API request failed; {e}"


def recognize_from_mic(language="en-US"):
    """Recognize live speech from the microphone."""
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Calibrating for background noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            recognizer.pause_threshold = 1

            print("Listening... Speak now!")
            audio = recognizer.listen(source)

        print("Processing speech...")
        text = recognizer.recognize_google(audio, language=language)
        return text

    except AttributeError:
        return "Error: PyAudio is not installed or no microphone detected."
    except sr.UnknownValueError:
        return "Could not understand the spoken audio."
    except sr.RequestError as e:
        return f"API request failed; {e}"


def main():
    print("=== Speech to Text ===")
    choice = input("Choose input source (1 = File, 2 = Microphone): ")

    lang_choice = input(
        "Choose language (1 = English [default], 2 = Persian/Farsi): "
    )
    language = "fa-IR" if lang_choice == "2" else "en-US"

    if choice == "1":
        filename = input("Enter file path (e.g., voice.wav): ")
        text = recognize_from_file(filename, language=language)

    elif choice == "2":
        text = recognize_from_mic(language=language)

    else:
        print("Invalid choice.")
        return

    print("\n--- Recognized Text ---\n")
    print(text)


if __name__ == "__main__":
    main()
