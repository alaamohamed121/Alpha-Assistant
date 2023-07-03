from ast import While
from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS

import speech_recognition as sr
import os
from art import *
from win32com.client import Dispatch
import time
from time import sleep, time
from bs4 import BeautifulSoup
import requests
import datetime
from googlesearch import search
import webbrowser
import webbrowser as wb


speak = Dispatch("SAPI.SpVoice").Speak
a = tprint("hello")

speak("Welcome to our program... I hope you have a happy experience with Alpha.. your personal assistant  please enter your id and password")
user_username  = input("username:")
user_pass = input("pass:")

name = "alaa"

def recordvoice():
    a = tprint("hello")

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say Something')
        try:
            audio = r.listen(source)
            print(audio)  # This is just a speech_recognition.AudioData object
            # Speech to text google recognizer
            user_input = r.recognize_google(audio)

            print(user_input)  # This is what you actually said
        except:
            print("sorry")
            speak("i cannot hear you can you say it again please")

    if "exit" in user_input:
        speak(f"goodbye mr {name}")
        exit()
    elif "hi" in user_input or "hello" in user_input:
        speak("hello , how can i help you")

    
    elif "old" in user_input or "how old are you" in user_input:
        speak("I was programmed in 2022 so I can say I was born in this year")
        speak("if you want another thing please tell me")

    elif "hi" in user_input:
        speak("hi... i hope you are good")
    elif "Your name" in user_input or "what is your name" in user_input or "Your name" in user_input:
        speak(
            "my name is  alpha ... and i am your assistant .")
        speak("if you want another thing please tell me")

    elif "Where do you live" in user_input or "you live" in user_input:
        speak(
            "I currently live on your computer,.. but if you live from my main source,.. I live in Egypt")
        speak("if you want another thing please tell me")

    elif "created you" in user_input or "made you" in user_input:
        speak(
            "I was created by Mr. Alaa Mohamed,.. the main developer of my program")
        speak("if you want another thing please tell me")

    elif "Do you love me" in user_input or "love me" in user_input:
        speak(
            "Of course I love you...because man is the reason for my existence")
        speak("if you want another thing please tell me")

    elif "How are you" in user_input or "What's up" in user_input:
        speak("I'm fine...thank you for your question. I hope you're fine too")
        speak("if you want another thing please tell me")

    elif "single" in user_input or "Are you in a relationship" in user_input:
        speak(
            "No, I'm just a computer program ..that can't enter into a relationship")
        speak("if you want another thing please tell me")

    elif "Egypt" in user_input or "what is your opinion about Egypt" in user_input or "egypt" in user_input:
        speak("Egypt is a very beautiful country, ..and according to statistics,.. it is growing at an incredible speed,.. and it seems that it will return to the era of power again.")
        speak("if you want another thing please tell me")

    elif "What's your gender" in user_input or "gender" in user_input:
        speak(
            "Actually, I'm a computer program,... but I use a man's voice to communicate with humans")
        speak("if you want another thing please tell me")

    elif "phone number" in user_input or "Do you have phone number" in user_input:
        speak(
            "No, but my developers allowed me to give his number to users... +201033466864")
        speak("if you want another thing please tell me")
    elif "help" in user_input:
        speak("i am here to help you so")
    elif "Shut down" in user_input or "shut down" in user_input:
        os.system("shutdown /s /t 1")
        speak("your pc will shut down now ...goodbye sir")
        exit()
    elif "Restart" in user_input or "restart" in user_input:
        os.system("shutdown /r /t 1")
        speak("your pc will restart now")
        exit()
    elif "weather" in user_input:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        def weather(city):
            city = city.replace(" ", "+")
            res = requests.get(
                f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
            print("Searching...\n")
            speak("Searching...\n")
            soup = BeautifulSoup(res.text, 'html.parser')
            location = soup.select('#wob_loc')[0].getText().strip()
            time = soup.select('#wob_dts')[0].getText().strip()
            info = soup.select('#wob_dc')[0].getText().strip()
            weather = soup.select('#wob_tm')[0].getText().strip()
            print(location)
            speak(location)
            print(time)
            speak(time)
            print(info)
            speak(info)
            print(weather+"°C")
            speak(weather+"°C")
        city = input("Enter the Name of City -> ")
        city = city+" weather"
        weather(city)
        print("Have a Nice Day:)")
        speak("Have a Nice Day:)")
        speak("if you need something else...please tell me")
    elif "time" in user_input:
        currentDT = datetime.datetime.now()
        speak("time now is ")

        print("Current Hour is: %d" % currentDT.hour)
        speak("Current Hour is: %d" % currentDT.hour)
        print("Current Minute is: %d" % currentDT.minute)
        speak("Current Minute is: %d" % currentDT.minute)
        print("Current Second is: %d" % currentDT.second)
        speak("Current Second is: %d" % currentDT.second)

    elif "date" in user_input or "data today" in user_input:
        currentDT = datetime.datetime.now()
        speak("today date is ")
        print("today date is ")

        print("Current Year is: %d" % currentDT.year)
        speak("Current Year is: %d" % currentDT.year)
        print("Current Month is: %d" % currentDT.month)
        speak("Current Month is: %d" % currentDT.month)     

        print("Current Day is: %d" % currentDT.day)
        speak("Current Day is: %d" % currentDT.day)
        speak("if you need something else...please tell me")
    elif "Microsoft Edge" in user_input or "Edge" in user_input:
        os.startfile('msedge')
        speak("open microsoft edge")
        speak("if you want another thing please tell me")
    elif "Google Chrome" in user_input or "Chrome" in user_input:
        os.startfile('chrome')
        speak("open google chrome")
        speak("if you want another thing please tell me")

    elif "Search" in user_input or "search" in user_input:

        speak(f"searching about {user_input}")
        print(".")
        print(".")
        print(".")
        wb.register('msedge', None)
        wb.open(user_input)

    elif "Get" in user_input or "get" in user_input:
        query_1 = user_input

        for result in search(query_1, num=20, stop=10):
            print(result)

        speak(
            "this websites will help you ...and if you need something else...please tell me")
    elif "Open" in user_input or "open" in user_input:
        query = user_input
        speak(
            f"we are opening {query} now ..if you need another thing please tell me")
        a = list(search(query, num=20, stop=10))
        url = a[0]
        webbrowser.open_new(url)

    elif "Tell me" in user_input or "tell me" in user_input:
        query = user_input
        speak(
            f"we are opening {query} now ..if you need another thing please tell me")
        a = list(search(query, num=20, stop=10))
        url = a[0]
        webbrowser.open_new(url)

    else:

        speak(
            f"sorry..but i cannot understand {user_input} ....you can use different word and tell me")


def wriitenreconnization():
    speak("how can i help you")
    user_input = input("how can i help you > :")
    if user_input == "e":
        speak(f"good bye mr.{name}")
        exit()

    split_sentence = user_input.split(' ')

    if "old" in user_input or "how old are you" in user_input:
        speak("I was programmed in 2022 so I can say I was born in this year")
        speak("if you want another thing please tell me")

    elif "hi alpha" in user_input:
        speak("hi... i hope you are good")
    elif "your name" in user_input or "what is your name" in user_input:
        speak(
            "my name is  alpha ... and i am your assistant .")
        speak("if you want another thing please tell me")

    elif "where do you live" in user_input or "you live" in user_input:
        speak("I currently live on your computer,.. but if you live from my main source,.. I live in Egypt")
        speak("if you want another thing please tell me")

    elif "created you" in user_input or "made you" in user_input:
        speak("I was created by Mr. Alaa Mohamed,.. the main developer of my program")
        speak("if you want another thing please tell me")

    elif "do you love me" in user_input or "love me" in user_input:
        speak("Of course I love you...because man is the reason for my existence")
        speak("if you want another thing please tell me")

    elif "how are you" in user_input or "what's up" in user_input:
        speak("I'm fine...thank you for your question. I hope you're fine too")
        speak("if you want another thing please tell me")

    elif "single" in user_input or "are you in a relationship" in user_input:
        speak("No, I'm just a computer program ..that can't enter into a relationship")
        speak("if you want another thing please tell me")

    elif "egypt" in user_input or "what is your opinion about Egypt" in user_input:
        speak("Egypt is a very beautiful country, ..and according to statistics,.. it is growing at an incredible speed,.. and it seems that it will return to the era of power again.")
        speak("if you want another thing please tell me")

    elif "what's your gender" in user_input or "gender" in user_input:
        speak("Actually, I'm a computer program,... but I use a man's voice to communicate with humans")
        speak("if you want another thing please tell me")

    elif "phone number" in user_input or "do you have phone number" in user_input:
        speak(
            "No, but my developers allowed me to give his number to users... +201033466864")
        speak("if you want another thing please tell me")
    elif "help" in user_input:
        speak("i am here to help you so")
    elif "shut down" in user_input:
        os.system("shutdown /s /t 1")
        speak("your pc will shut down now ...goodbye sir")
        exit()
    elif "restart" in user_input:
        os.system("shutdown /r /t 1")
        speak("your pc will restart now")
        exit()
    elif "weather" in user_input:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        def weather(city):
            city = city.replace(" ", "+")
            res = requests.get(
                f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
            print("Searching...\n")
            speak("Searching...\n")
            soup = BeautifulSoup(res.text, 'html.parser')
            location = soup.select('#wob_loc')[0].getText().strip()
            time = soup.select('#wob_dts')[0].getText().strip()
            info = soup.select('#wob_dc')[0].getText().strip()
            weather = soup.select('#wob_tm')[0].getText().strip()
            print(location)
            speak(location)
            print(time)
            speak(time)
            print(info)
            speak(info)
            print(weather+"°C")
            speak(weather+"°C")
        city = input("Enter the Name of City -> ")
        city = city+" weather"
        weather(city)
        print("Have a Nice Day:)")
        speak("Have a Nice Day:)")
        speak("if you need something else...please tell me")
    elif "time" in user_input:
        currentDT = datetime.datetime.now()
        speak("time now is ")

        print("Current Hour is: %d" % currentDT.hour)
        speak("Current Hour is: %d" % currentDT.hour)
        print("Current Minute is: %d" % currentDT.minute)
        speak("Current Minute is: %d" % currentDT.minute)
        print("Current Second is: %d" % currentDT.second)
        speak("Current Second is: %d" % currentDT.second)

    elif "date" in user_input or "data today" in user_input:
        currentDT = datetime.datetime.now()
        speak("today date is ")
        print("today date is ")

        print("Current Year is: %d" % currentDT.year)
        speak("Current Year is: %d" % currentDT.year)
        print("Current Month is: %d" % currentDT.month)
        speak("Current Month is: %d" % currentDT.month)

        print("Current Day is: %d" % currentDT.day)
        speak("Current Day is: %d" % currentDT.day)
        speak("if you need something else...please tell me")
    elif "microsoft edge" in user_input or "edge" in user_input:
        os.startfile('msedge')
        speak("open microsoft edge")
        speak("if you want another thing please tell me")
    elif "google chrome" in user_input or "chrome" in user_input:
        os.startfile('chrome')
        speak("open google chrome")
        speak("if you want another thing please tell me")

    elif "search" in user_input:

        speak(f"searching about {user_input}")
        print(".")
        print(".")
        print(".")
        wb.register('msedge', None)
        wb.open(user_input)

    elif "get" in user_input:
        query_1 = user_input

        for result in search(query_1, num=20, stop=10):
            print(result)

        speak(
            "this websites will help you ...and if you need something else...please tell me")
    elif "open" in user_input:
        query = user_input
        speak(
            f"we are opening {query} now ..if you need another thing please tell me")
        a = list(search(query, num=20, stop=10))
        url = a[0]
        webbrowser.open_new(url)
    elif "tell me" in user_input:
        query = user_input
        print("searching....")
        print("get result...")
        speak(
            f"this article will help you..if you need another thing please tell me")
        a = list(search(query, num=20, stop=10))
        url = a[0]
        webbrowser.open_new(url)

    else:

        speak(
            f"sorry..but i cannot understand {user_input} ....you can use different word and tell me")


def loop():
    user_1 = input(
        "do you want to record or write type (Record (r) or Written (w) or Exit (e)):").capitalize()

    if user_1 == "W":
        while TRUE:
            wriitenreconnization()

    elif user_1 == "R":
        while TRUE:
            recordvoice()
    elif user_1 == "E":
        speak(f"good bye MR.{name}")
        exit()

    else:
        speak("sorry you input wrong choise... please try again")
        loop()


if user_username == "alaa" and user_pass == "alaa123":
    loop()
else:
    print("you donot have permission to access to my program")