import os
import voice
import speech_recognition
import voice_actions
import pyttsx3

if __name__ == '__main__':

    recognizer = speech_recognition.Recognizer()
    micro = speech_recognition.Microphone()
    voice_work = voice_actions.WorkingWithVoice()

    # initializing the speech synthesis tool
    ttsEngine = pyttsx3.init()

    # set parametrs of our assistent
    assistent = voice.VoiceAssistant()
    assistent.set_name('Alice')
    assistent.set_sex('female')
    assistent.set_speech_language('ru')

    # setting the default voice
    assistent.setup_assistant_voice(ttsEngine=ttsEngine)

    while True:
        # start of speech recording with subsequent output of recognized speech
        # and deleting the audio recorded in the microphone
        voice_input = voice_work.record_and_recognize(microphone=micro, recognizer=recognizer)
        os.remove('microphone-results.wav')
        print(voice_input)

        # отделение комманд от дополнительной информации (аргументов)
        voice_input = voice_input.split(" ")
        command = voice_input[0]

        if command == "привет":
            assistent.play_voice_assistant_speech("Здравствуй")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
