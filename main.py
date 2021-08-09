import speech_recognition
import recording_and_recognizing

if __name__ == '__main__':
    recognizer = speech_recognition.Recognizer()
    micro = speech_recognition.Microphone()


    while True:
        voice_input = record_and_recognize_audio()
        print(voice_input)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
