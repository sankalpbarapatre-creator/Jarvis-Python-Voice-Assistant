import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

r = sr.Recognizer()
newsapi = "Your_Api_Key"

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def process(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")  
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com") 
    elif "open facebook" in c.lower():
            webbrowser.open("https://facebook.com") 
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]     
        webbrowser.open(link)   

    elif "news" in c.lower() :     
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:

            data = r.json()

            articles = data.get('articles', [])

            for article in articles:
                speak(article['title'])


if __name__== "__main__":
    speak("Initializing jarvis...")
    while True:
        # listen for the wake word jarvis
        # obtain audio from the microphone
        
        print("Recognizing...")    
        try:
            with sr.Microphone(device_index=2) as source:   
                    print("Please wait...")
                    r.adjust_for_ambient_noise(source, duration=0.2)

                    print("Listening...")
                    audio = r.listen(source)
            command = r.recognize_google(audio)
            if(command.lower() == "jarvis"):
                speak("Ya")

                #Listen for command
                with sr.Microphone(device_index=2) as source:   
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    print ("jarvis active...")
                    audio = r.listen(source,timeout=5,phrase_time_limit=2)
                    command = r.recognize_google(audio)

                    process(command)


        except Exception as e:
            print("Error;{0}".format(e))
