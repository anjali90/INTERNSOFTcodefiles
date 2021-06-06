#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install SpeechRecognition


# In[2]:


pip install pyttsx3


# In[3]:


conda install -c conda-forge wikipedia


# In[4]:


pip install wolframalpha


# In[5]:


pip install instaloader


# In[ ]:


conda install -c anaconda comtypes


# In[8]:


pip install comtypes


# In[7]:


conda install -c anaconda pyaudio


# In[9]:


import os
import time
import subprocess
import json


# In[10]:


import wolframalpha
import requests
import webbrowser
import wikipedia
import datetime


# In[11]:


import speech_recognition as sr
import pyttsx3


# In[12]:


print('LOADING YOUR A.I PERSONAL ASSISTANT JARVIS')


# In[13]:


import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",'voices[0].id')


# In[14]:


def speak(text):
    engine.say(text)
    engine.runAndWait()


# In[15]:


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning Mr.JARVIS")
        print("Hello, Good Morning Mr.JARVIS")
    elif hour >= 12 and hour <= 18:
        speak("Hello, Good Afternoon Mr. JARVIS")
        print("Hello, Good Afternoon Mr. JARVIS")
    else:
        speak("It's already the night time, better go to sleep")
        print("It's already the night time, better go to sleep")


# In[16]:


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I Am Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio,language = 'en-in')
            print(f"User said:{statement}\n")

        except Exception as e:
                speak("Pardon me, please say that again")
                return "None"
        return statement


# In[17]:


speak("LOADING YOUR PERSONAL A.I ASSISTANT JARVIS")
wishMe()


# In[ ]:


if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue
            
        if "Good Bye" in statement or "Ok Bye" in statement or "Stop" in statement:
            speak("Your Personal A.I Assitant JARVIS is shutting down, Good Bye")
            print("Your Personal A.I Assitant JARVIS is shutting down, Good Bye")
            break
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", " ")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak("city not found")
                print("city not found")
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif "who are you" in statement or "what can you do" in statement:
            speak("I am JARVIS your personal assistant. I am programmed to do minor tasks")
        elif "who made you" in statement or " who created you" in statement or "who discovered you" in statement:
            speak("i was built by ironman")
            print("i was built by ironman")
         
        elif "open stack overflow" in statement:
                webbrowser.open_new_tab("https:..stackoverflow.com/login")
                time.sleep(5)
        elif "news" in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("here are some headlines for you from times of India - Happy reading")
            time.sleep(7)
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
            
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="Paste your unique ID here "
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        elif "log off" in statement or "sign out" in statement or "shut down" in statement:
            speak("ok, your pc will shut down in 10seconds - make sure you have saved and exit from all application ")
            subprocess.call(['shutdown',"/1"])
            
time.sleep(3)
            
                
                
                
                
                
                


# In[ ]:





# In[ ]:




