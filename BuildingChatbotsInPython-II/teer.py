import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyttsx3

def assistant(response):
    print(response)
    assistantvoice(response)  # ใช้สำหรับพูดเสียง

def assistantvoice(audio): 
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # เลือกเสียงผู้หญิง
    engine.say(audio)
    engine.runAndWait()

def audioinput():
    aud = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening and processing...')
        aud.pause_threshold = 0.7
        audio = aud.listen(source)
        
        try:
            print("Understanding...")
            phrase = aud.recognize_google(audio, language='en-US')
            print("You said: ", phrase)
        except Exception as exp:
            print(exp)
            print("Can you please repeat that")
            return "None"
    
    return phrase

def theDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {
        1: 'Monday', 
        2: 'Tuesday',
        3: 'Wednesday', 
        4: 'Thursday',
        5: 'Friday', 
        6: 'Saturday',
        7: 'Sunday'
    }
    
    if day in Day_dict.keys():
        weekday = Day_dict[day]
        print(weekday)
        assistant("It's " + weekday)

def theTime():
    time = str(datetime.datetime.now())
    hour = time[11:13]
    min = time[14:16]
    assistant("The time right now is " + hour + " Hours and " + min + " Minutes")

# Main loop for the virtual assistant
while True:
    phrase = audioinput().lower()

    if "what is your name" in phrase:
        assistant("I am your nameless virtual assistant")
        continue

    elif "bye" in phrase:
        assistant("Exiting. Have a good day!")
        break

    elif "what day is it" in phrase:
        theDay()
        continue

    elif "what time is it" in phrase:
        theTime()
        continue

    elif "open google" in phrase:
        assistant("Opening Google")
        webbrowser.open("https://www.google.com")
        continue

    elif "open youtube" in phrase:
        assistant("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        continue

    elif "wiki" in phrase:
        assistant("Checking Wikipedia")
        phrase = phrase.replace("wiki ", "")
        result = wikipedia.summary(phrase, sentences=4)
        assistant("As per Wikipedia")
        assistant(result)
        continue
    
    elif "play" in phrase:
        video_title = phrase.replace("play ", "")
        assistant(f"Searching for {video_title} on YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={video_title}")
        continue