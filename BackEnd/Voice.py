import speech_recognition as sr


def getSpeech():
       # obtain audio from the microphone
       r = sr.Recognizer()
       with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, 7, 7)
        print ("Processing...")

       try:   # using google speech recognition
        return r.recognize_google(audio)
       except:
        return "Sorry, I did not get that"