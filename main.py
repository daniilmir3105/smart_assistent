import os
import voice
import speech_recognition
import voice_actions
import pyttsx3
import voice_commands
import person
import objects

if __name__ == '__main__':
    object1 = objects.Object()
    commands = voice_commands.BotCommands()
    recognizer = speech_recognition.Recognizer()
    micro = speech_recognition.Microphone()
    voice_work = voice_actions.WorkingWithVoice()
    assistant = object1.get_assistent()

    while True:
        # start of speech recording with subsequent output of recognized speech
        # and deleting the audio recorded in the microphone
        voice_input = voice_work.record_and_recognize(microphone=micro, recognizer=recognizer)
        os.remove('microphone-results.wav')
        print(voice_input)

        # отделение комманд от дополнительной информации (аргументов)
        voice_input = voice_input.split(" ")
        command = voice_input[0]
        command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
        commands.execute_command_with_name(command, command_options)

        if command == "привет":
            assistant.play_voice_assistant_speech("Здравствуй")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
