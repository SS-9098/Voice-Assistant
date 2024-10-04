import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
 print("Say something!")
 audio = r.listen(source, 10, 10)
 print ("Processing...")

try:   # using google speech recognition
 print("Text: "+r.recognize_google(audio))
except:
 print("Sorry, I did not get that")