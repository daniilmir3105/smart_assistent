# import making_commands
# import person
import 
import translator

class BotCommands:
    '''
    This class will have field for our voice-commands
    and method for processing.
    '''

    __maker =
    __translator = translator.Translation()
    __person =

    __commands = {
    ("hello", "hi", "morning", "привет"): __maker.play_greetings(translator=__translator, person=__person),
    ("bye", "goodbye", "quit", "exit", "stop", "пока"): __maker.play_farewell_and_quit(translator=__translator, person=__person),
    ("search", "google", "find", "найди"): __maker.search_for_term_on_google(),
    ("video", "youtube", "watch", "видео"): __maker.search_for_video_on_youtube(),
    ("wikipedia", "definition", "about", "определение", "википедия"): __maker.search_for_definition_on_wikipedia(),
    ("translate", "interpretation", "translation", "перевод", "перевести", "переведи"): __maker.get_translation(),
    ("language", "язык"): __maker.change_language(),
    ("weather", "forecast", "погода", "прогноз"): __maker.get_weather_forecast(),
    }

    def execute_command_with_name(self, command_name: str, *args: list):
        """
        Выполнение заданной пользователем команды с дополнительными аргументами
        :param command_name: the name of the commnd
        :param args: arguments, that will be used in our method
        :return:
        """
        for key in self.__commands.keys():
            if command_name in key:
                self.__commands[key](*args)
            else:
                pass  # print("Command not found")