#Imports the SpeechRecognition library, which is used to recognize voice commands.
import speech_recognition as sr
# Imports the datetime library, which is used to get the current time.
import datetime
#Imports the subprocess library, which is used to open Google Chrome.
import subprocess
#Text to speech conversion
import pyttsx3
#used to open the browser
import webbrowser
#It is used to play a video on youtube
import pywhatkit


#this initializes the text-to-speech engine
engine=pyttsx3.init()
#this gets the list of available voices
voices=engine.getProperty('voices')
#Sets the voice of the text-to-speech engine to the second voice in the list.
engine.setProperty('voices',voices[0].id)
#Initializes the recognizer object from the SpeechRecognition library.
recognizer=sr.Recognizer()

def cmd():
    #this uses the microphone as the source of video recording
    with sr.Microphone() as source:
        print('Clearing background noises...')
    #Adjusts the recognizer for ambient noise for better speech recognition.
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('Ask me anything')
    #Records audio from the microphone and stores it in the 'recordedaudio' variable.
        recordedaudio=recognizer.listen(source)
    
    text = ""
    try:
    #recognizes the text from the recorded audio using the Google Speech Recognition API and stores it in the 'text' variable.
        text=recognizer.recognize_google(recordedaudio,language='en_US')
    #text converts to lowercase for better matching keywords.
        text=text.lower()
        print('Your message:',format(text))

        if 'goodbye' in text:
                    print("Exiting the program...")
                    engine.say("Goodbye")
                    engine.runAndWait()
                    exit(0)

    except Exception as ex:
        print("Sorry, I didn't quite catch that.")
        

    if 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say(time)
        engine.runAndWait()
    if 'play' in text:
        a='opening youtube..'
        engine.say(a)
        engine.runAndWait()
        pywhatkit.playonyt(text)
    if 'youtube' in text:
        b='opening youtube'
        engine.say(b)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')
 
while True:
    cmd()
