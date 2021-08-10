import os
import voice
import speech_recognition
import voice_actions

if __name__ == '__main__':
    recognizer = speech_recognition.Recognizer()
    micro = speech_recognition.Microphone()
    voice_work = voice_actions.WorkingWithVoice()

    while True:
        # start of speech recording with subsequent output of recognized speech
        # and deleting the audio recorded in the microphone
        voice_input = voice_work.record_and_recognize(microphone=micro, recognizer=recognizer)
        os.remove('microphone-results.wav')
        print(voice_input)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
