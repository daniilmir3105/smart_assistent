import speech_recognition

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