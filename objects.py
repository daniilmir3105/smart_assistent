import person
# import translator
import voice
import pyttsx3


# configuring user data
person = person.OwnerPerson()
person.set_name("Tanya")
person.set_home_city("Yekaterinburg")
person.set_native_language("ru")
person.set_target_language("en")

# set parametrs of our assistent
assistent = voice.VoiceAssistant()
assistent.set_name('Alice')
assistent.set_sex('female')
assistent.set_speech_language('ru')

# initializing the speech synthesis tool
ttsEngine = pyttsx3.init()

# setting the default voice
assistent.setup_assistant_voice(ttsEngine=ttsEngine)