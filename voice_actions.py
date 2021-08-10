# import speech_recognition
from vosk import Model, KaldiRecognizer  # offline-recogntion with Vosk
import speech_recognition  # user speech recognition (Speech-To-Text)
import wave  # creating and reading wav audio files
import json  # working with json files and json strings
import os  # working with the file system

class WorkingWithVoice:
    '''
    This is the class for work with voice.
    For example for recording and recognizing.
    '''

    def record_and_recognize(self, microphone, recognizer):
        '''
        This method is for voice-recording and voice-recognizing
        :param args: microphone(type:
        :return: recognized_data(type: string)
        '''

        with microphone:
            recognized_data = ''

            # regulating microphone volume
            recognizer.adjust_for_ambient_noise(microphone, duration=2)

            try:
                print('Listening...')
                audio = recognizer.listen(microphone, 5, 5)
            except speech_recognition.WaitTimeoutError:
                print("Can you check if your microphone is on, please?")
                return

            try:
                print('Starting recognition...')
                recognized_data = recognizer.recognize_google(audio, language="ru").lower()
            except speech_recognition.UnknownValueError:
                # print('')
                pass

            # in situation with internet-connection except this error
            except speech_recognition.RequestError:
                print("Check your Internet Connection, please")

        return recognized_data

    def use_offline_recognition(self):
        '''
        Switching to offline speech recognition
        :return: recognized phrase
        '''

        recognized_data = ''

        try:
            # checking the availability of the model in the desired language in the application catalog
            if not os.path.exist('models/vosk-model-small-ru-0.4'):
                print("Please download the model from:\nhttps://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
                exit(1)

            # analyzing the audio recorded in the microphone (to avoid repeating the phrase)
            wave_audio_file = wave.open('microphone-results.wav', 'rb')
            model = Model('models/vosk-model-small-ru-0.4')
            offline_recognizer = KaldiRecognizer(model, wave_audio_file.getnframes())
            data = wave_audio_file.readframes(wave_audio_file.getnframes())
            if len(data) > 0:
                if offline_recognizer.AcceptWaveform(data):
                    recognized_data = offline_recognizer.Result()

                    # getting recognized text data from a JSON string
                    # (so that you can give an answer to it)
                    recognized_data = json.loads(recognized_data)
                    recognized_data = recognized_data["text"]
        except:
            print('Sorry, speech service is unavailable. Try again later')

        return recognized_data