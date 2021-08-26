import voice
import random
import pyttsx3
import webbrowser
from googlesearch import search
import traceback
import wikipediaapi
import googletrans
from termcolor import colored
from pyowm import OWM
import os

class Making:
    '''
    This class will have methods,
    '''

    __speaking = voice.VoiceAssistant()

    def play_greetings(self, translator, person, *args: tuple):
        """
        Playing a random welcome speech.
        """
        greetings = [
            translator.get("Hello, {}! How can I help you today?").format(person.get_name()),
            translator.get("Good day to you {}! How can I help you today?").format(person.get_name())
        ]
        self.__speaking.play_voice_assistant_speech(greetings[random.randint(0, len(greetings) - 1)])

    def play_farewell_and_quit(self, translator, person, *args: tuple):
        """
        Playing a farewell speech and leaving.
        """
        farewells = [
            translator.get("Goodbye, {}! Have a nice day!").format(person.name),
            translator.get("See you soon, {}!").format(person.name)
        ]
        self.__speaking.play_voice_assistant_speech(farewells[random.randint(0, len(farewells) - 1)])
        ttsEngine = pyttsx3.init()
        ttsEngine.stop()
        quit()

    def search_for_term_on_google(self, translator, assistant, *args: tuple):
        """
        Google search with automatic opening of links
        (to the list of results and to the results themselves,
        if possible).
        :param args: search query phrase
        """
        if not args[0]: return
        search_term = " ".join(args[0])

        # opening a link to a search engine in the browser
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)

        # альтернативный поиск с автоматическим открытием ссылок на результаты (в некоторых случаях может быть небезопасно)
        search_results = []
        try:
            for _ in search(search_term,  # что искать
                            tld="com",  # верхнеуровневый домен
                            lang=assistant.get_speech_language(),  # используется язык, на котором говорит ассистент
                            num=1,  # количество результатов на странице
                            start=0,  # индекс первого извлекаемого результата
                            stop=1,
                            # индекс последнего извлекаемого результата (я хочу, чтобы открывался первый результат)
                            pause=1.0,  # задержка между HTTP-запросами
                            ):
                search_results.append(_)
                webbrowser.get().open(_)

        # поскольку все ошибки предсказать сложно, то будет произведен отлов с последующим выводом без остановки программы
        except:
            self.__speaking.play_voice_assistant_speech(translator.get("Seems like we have a trouble. See logs for more information"))
            traceback.print_exc()
            return

        print(search_results)
        self.__speaking.play_voice_assistant_speech(translator.get("Here is what I found for {} on google").format(search_term))

    def search_for_video_on_youtube(self, translator, *args: tuple):
        """
        Search for videos on YouTube with automatic opening of a link to the list of results
        :param args: search query phrase
        """
        if not args[0]: return
        search_term = " ".join(args[0])
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        self.__speaking.play_voice_assistant_speech(translator.get("Here is what I found for {} on youtube").format(search_term))

    def search_for_definition_on_wikipedia(self, translator, assistant, *args: tuple):
        """
        Search for definitions in Wikipedia, followed by voicing the results and opening links
        :param args: search query phrase
        """
        if not args[0]: return

        search_term = " ".join(args[0])

        # setting the language (in this case, the language spoken by the assistant is used)
        wiki = wikipediaapi.Wikipedia(assistant.speech_language)

        # search for a page by query, read summary, open a link to the page for detailed information
        wiki_page = wiki.page(search_term)
        try:
            if wiki_page.exists():
                self.__speaking.play_voice_assistant_speech(
                    translator.get("Here is what I found for {} on Wikipedia").format(search_term))
                webbrowser.get().open(wiki_page.fullurl)

                # the assistant reads the first two sentences of summary from the Wikipedia page
                # (there may be problems with multilingualism)
                self.__speaking.play_voice_assistant_speech(wiki_page.summary.split(".")[:2])
            else:
                # opening a link to a search engine in the browser if nothing could be found on Wikipedia for the query
                self.__speaking.play_voice_assistant_speech(translator.get(
                    "Can't find {} on Wikipedia. But here is what I found on google").format(search_term))
                url = "https://google.com/search?q=" + search_term
                webbrowser.get().open(url)

        # since it is difficult to predict all errors, it will be captured and then output without stopping the program
        except:
            self.__speaking.play_voice_assistant_speech(translator.get("Seems like we have a trouble. See logs for more information"))
            traceback.print_exc()
            return

    def get_translation(self, assistant, person, translator, *args: tuple):
        """
        Getting a translation of a text from one language to another (in this case, from the one being studied to the native language or back)
        :param args: the phrase that you want to translate
        """
        if not args[0]: return

        search_term = " ".join(args[0])
        google_translator = googletrans.Translator()
        translation_result = ""

        old_assistant_language = assistant.speech_language
        try:
            # if the assistant's speech language and the user's native language differ, then the translation is performed into the native language
            if assistant.speech_language != person.native_language:
                translation_result = google_translator.translate(search_term,  # what to translate
                                                                 src=person.target_language,  # from what language
                                                                 dest=person.native_language)  # in what language

                self.__speaking.play_voice_assistant_speech("The translation for {} in Russian is".format(search_term))

                # changing the assistant's voice to the user's native language (so that the translation can be pronounced)
                assistant.speech_language = person.native_language
                self.__speaking.setup_assistant_voice()

            # if the assistant's speech language and the user's native language are the same, then the translation is performed into the language being studied
            else:
                translation_result = google_translator.translate(search_term,  # what to translate
                                                                 src=person.native_language,  # from what language
                                                                 dest=person.target_language)  # in what language
                self.__speaking.play_voice_assistant_speech("По-английски {} будет как".format(search_term))

                # changing the assistant's voice to the user's language being studied (so that the translation can be pronounced)
                assistant.speech_language = person.target_language
                self.__speaking.setup_assistant_voice()

            # pronouncing the translation
            self.__speaking.play_voice_assistant_speech(translation_result.text)

        # since it is difficult to predict all errors, it will be captured and then output without stopping the program
        except:
            self.__speaking.play_voice_assistant_speech(translator.get("Seems like we have a trouble. See logs for more information"))
            traceback.print_exc()

        finally:
            # return to the previous settings of the assistant's voice
            assistant.speech_language = old_assistant_language
            self.__speaking.setup_assistant_voice()

    def change_language(self, assistant, *args: tuple):
        """
        Changing the language of the voice assistant (speech recognition language)
        """
        assistant.speech_language = "ru" if assistant.speech_language == "en" else "en"
        self.__speaking.setup_assistant_voice()
        print(colored("Language switched to " + assistant.speech_language, "cyan"))

    def get_weather_forecast(self, person, translator, *args: tuple):
        """
        Getting and voicing the weather forecast
        :param args: the city for which the zapos should be performed
        """
        # if there is an additional argument , the weather request is made using it,
        # otherwise, the city specified in the settings is used
        if args[0]:
            city_name = args[0][0]
        else:
            city_name = person.home_city

        try:
            # using the API key placed in the. env file for example WEATHER_API_KEY = "01234abcd....."
            weather_api_key = os.getenv("53e1dec3517a7f5e30251ccbb9049d18")
            open_weather_map = OWM(weather_api_key)

            # запрос данных о текущем состоянии погоды
            weather_manager = open_weather_map.weather_manager()
            observation = weather_manager.weather_at_place(city_name)
            weather = observation.weather

        # since it is difficult to predict all errors, it will be captured and then output without stopping the program
        except:
            self.__speaking.play_voice_assistant_speech(translator.get("Seems like we have a trouble. See logs for more information"))
            traceback.print_exc()
            return

        # splitting data into parts for the convenience of working with them
        status = weather.detailed_status
        temperature = weather.temperature('celsius')["temp"]
        wind_speed = weather.wind()["speed"]
        pressure = int(weather.pressure["press"] / 1.333)  # translated from gPA to mmHg.

        # output of logs
        print(colored("Weather in " + city_name +
                      ":\n * Status: " + status +
                      "\n * Wind speed (m/sec): " + str(wind_speed) +
                      "\n * Temperature (Celsius): " + str(temperature) +
                      "\n * Pressure (mm Hg): " + str(pressure), "yellow"))

        # voicing the current state of the weather by an assistant (additional work is required here for multilingualism)
        self.__speaking.play_voice_assistant_speech(translator.get("It is {0} in {1}").format(status, city_name))
        self.__speaking.play_voice_assistant_speech(translator.get("The temperature is {} degrees Celsius").format(str(temperature)))
        self.__speaking.play_voice_assistant_speech(translator.get("The wind speed is {} meters per second").format(str(wind_speed)))
        self.__speaking.play_voice_assistant_speech(translator.get("The pressure is {} mm Hg").format(str(pressure)))