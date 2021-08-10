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

    def setup_assistent_voice(self):
        '''
        Setting the default voice (the index may change in
        depending on the operating system settings)
        :return:
        '''

        ttsEngine = pyttsx3.init()
        voices = ttsEngine.getProperty('voices')

        if assistant.speech_language == "en":
            assistant.recognition_language = "en-US"
            if assistant.sex == "female":
                # Microsoft Zira Desktop - English (United States)
                ttsEngine.setProperty("voice", voices[1].id)
            else:
                # Microsoft David Desktop - English (United States)
                ttsEngine.setProperty("voice", voices[2].id)
        else:
            assistant.recognition_language = "ru-RU"
            # Microsoft Irina Desktop - Russian
            ttsEngine.setProperty("voice", voices[0].id)

        pass

    def play_voice_assistant_speech(text_to_speech):
        """
        Проигрывание речи ответов голосового ассистента (без сохранения аудио)
        :param text_to_speech: текст, который нужно преобразовать в речь
        """
        ttsEngine = pyttsx3.init()
        ttsEngine.say(str(text_to_speech))
        ttsEngine.runAndWait()
