import speech_recognition
import voice_actions

if __name__ == '__main__':
    recognizer = speech_recognition.Recognizer()
    micro = speech_recognition.Microphone()
    voice_work = voice_actions.WorkingWithVoice()

    while True:
        voice_input = voice_work.record_and_recognize()
        print(voice_input)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
