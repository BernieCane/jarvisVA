import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        eel.DisplayMessage('Listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)
    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing....')
        query = r.recognize_google(audio, language='en-US')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
    except Exception as e:
        print(f"Error in takecommand: {e}")  # In lỗi nếu có
        return ""
    return query.lower()

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        print(query)  # In giá trị query
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        # Kiểm tra các lệnh
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        else:
            from engine.features import chatBot
            chatBot(query)

    except Exception as e:
        print(f"Error in allCommands: {e}")  # In lỗi nếu có

    eel.ShowHood()
