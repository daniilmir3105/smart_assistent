from vosk import Model, KaldiRecognizer  # оффлайн-распознавание от Vosk
import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
import pyttsx3  # синтез речи (Text-To-Speech)
import wave  # создание и чтение аудиофайлов формата wav
import json  # работа с json-файлами и json-строками
import os  # работа с файловой системой

class VoiceAssistant:
    '''
    Voice assistant settings, including name, gender, language of speech
    '''

    # fields

    __name = ''
    __sex = ''
    __speech_language = ''
    __recognition_language = ''

    # setters
    def set_name(self, string):
        '''
        This method will set name of assistant
        :param string: this variable will be name
        :return: __name
        '''

        self.__name = string
        return self.__name

    def set_sex(self, string):
        '''
        This method will set sex of assistant
        :param string: this variable will be sex
        :return: __sex
        '''

        self.__sex = string
        return self.__sex

    def set_speech_language(self, string):
        '''
        This method will set speech language of assistant.
        :param string: This variable will be speech language
        :return: __speech_language
        '''

        self.__speech_language = string
        return self.__speech_language

    def set_recognition_language(self, string):
        '''
        This method will set recognition language of assistant.
        :param string: This variable will be recognition language
        :return: __recognition_language
        '''

        self.__recognition_language = string
        return self.__recognition_language

    # getters
    def get_name(self):
        '''
        This method will get name of assistant
        :return: __name
        '''

        return self.__name

    def get_sex(self):
        '''
        This method will get sex of assistant
        :return: __sex
        '''

        return self.__sex

    def get_speech_language(self):
        '''
        This method will get speech language of assistant
        :return: __speech_language
        '''

        return self.__speech_language

    def get_recognition_language(self):
        '''
        This method will get recognition language of assistant
        :return: __recognition_language
        '''

        return self.__recognition_language

    def setup_assistant_voice(self, ttsEngine):
        '''
        Setting the default voice (the index may change in
        depending on the operating system settings)
        :return: setup of assistant
        '''

        voices = ttsEngine.getProperty('voices')

        if self.__recognition_language == "en":
            self.__recognition_language = "en-US"
            if self.__sex == "female":
                # Microsoft Zira Desktop - English (United States)
                ttsEngine.setProperty("voice", voices[1].id)
            else:
                # Microsoft David Desktop - English (United States)
                ttsEngine.setProperty("voice", voices[2].id)
        else:
            self.__recognition_language = "ru-RU"
            # Microsoft Irina Desktop - Russian
            ttsEngine.setProperty("voice", voices[0].id)

        # pass

    def play_voice_assistant_speech(text_to_speech):
        """
        Speech playback of voice assistant responses (without saving audio)
        :param text_to_speech: the text to be converted to speech
        """

        ttsEngine = pyttsx3.init()
        ttsEngine.say(str(text_to_speech))
        ttsEngine.runAndWait()
