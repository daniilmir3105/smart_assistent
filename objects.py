import person
# import translator
import voice
import pyttsx3

class Object:
    '''
    This class will have objects for our voice-assistant
    '''

    # configuring user data
    __person = person.OwnerPerson()
    __person.set_name("Daniil")
    __person.set_home_city("Saint Petersburg")
    __person.set_native_language("ru")
    __person.set_target_language("en")

    # set parametrs of our assistent
    __assistant = voice.VoiceAssistant()
    __assistant.set_name('Alice')
    __assistant.set_sex('female')
    __assistant.set_speech_language('ru')

    # initializing the speech synthesis tool
    ttsEngine = pyttsx3.init()

    # setting the default voice
    __assistant.setup_assistant_voice(ttsEngine=ttsEngine)

    def get_person(self):
        '''
        This method will return object(person)
        :return: object person
        '''

        return self.__person

    def get_assistent(self):
        '''
        This method will return object(person)
        :return: object assistant
        '''
        return self.__assistant