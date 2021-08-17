class bot_commands:
    '''
    This class will have field for our voice-commands
    and method for processing.
    '''

    __commands = {
    ("hello", "hi", "morning", "привет"): play_greetings,
    ("bye", "goodbye", "quit", "exit", "stop", "пока"): play_farewell_and_quit,
    ("search", "google", "find", "найди"): search_for_term_on_google,
    ("video", "youtube", "watch", "видео"): search_for_video_on_youtube,
    ("wikipedia", "definition", "about", "определение", "википедия"): search_for_definition_on_wikipedia,
    ("translate", "interpretation", "translation", "перевод", "перевести", "переведи"): get_translation,
    ("language", "язык"): change_language,
    ("weather", "forecast", "погода", "прогноз"): get_weather_forecast,
    }

    def execute_command_with_name(command_name: str, *args: list):
        """
        Выполнение заданной пользователем команды с дополнительными аргументами
        :param command_name: the name of the commnd
        :param args: arguments, that will be used in our method
        :return:
        """
        for key in commands.keys():
            if command_name in key:
                commands[key](*args)
            else:
                pass  # print("Command not found")