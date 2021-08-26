from termcolor import colored
import json
# from objects import assistent
import objects

class Translation:
    """
    Getting a string translation embedded in the application to create
    a multilingual assistant
    """

    object1 = objects.Object()
    __assistant = object1.get_assistent()

    with open("translations.json", "r", encoding="UTF-8") as file:
        translations = json.load(file)

    def get(self, text: str):
        """
        Getting a line feed from a file into the desired language (by its code)
        :param text: the text to be translated
        :return: text translation embedded in the application
        """
        if text in self.translations:
            return self.translations[text][self.__assistant.speech_language]
        else:
            # if there is no translation, a message about this is displayed in
            # the logs and the source text is returned
            print(colored("Not translated phrase: {}".format(text), "red"))
            return text