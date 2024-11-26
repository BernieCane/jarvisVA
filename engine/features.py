import os
from pipes import quote
import re
import struct
import time
from playsound import playsound
import eel
import pvporcupine
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import sqlite3
import webbrowser
import pyaudio
import pyautogui
import subprocess
from engine.helper import extract_yt_term
from hugchat import hugchat

@eel.expose
def playAssistantSound():
    music_dir ="www\\assets\\audio\\game-start-6104.mp3"
    playsound(music_dir)

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name, ))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("opening " + query)
                os.startfile(results[0][0])
            
            elif len(results) == 0:
                cursor.execute(
                    'SELECT url FROM web_command WHERE name IN (?)', (app_name, ))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("opening " + query)
                    webbrowser.open(results[0][0])

                else:
                    speak("opening " + query)
                    try:
                        os.system('start' +query)
                    except:
                        speak("not found")

        except:
            speak("something went wrong")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("playing " + search_term+" on youtube")
    kit.playonyt(search_term)


def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:

        #pre trained keywords
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"])
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)

        #loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            #processing keyword comes from mic
            keyword_index=porcupine.process(keyword)

            #checking first keyword detected for not
            if keyword_index>=0:
                print("Hotword detected")

                #pressing shortcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

#chat bot
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    speak(response)
    return response

#android automation
def makeCall(name, mobileNo):
    mobileNo = mobileNo.replace(" ", "")
    speak("calling " + name)
    command="adb shell am start -a android.intent.action.CALL -d tel:" + mobileNo
    os.system(command)