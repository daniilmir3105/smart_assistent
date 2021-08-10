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

    def setup_assistent_voice(self):
        '''
        Setting the default voice (the index may change in
        depending on the operating system settings)
        :return:
        '''