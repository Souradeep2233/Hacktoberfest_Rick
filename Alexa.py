import speech_recognition as sr
listener = sr.Recognizer()
with sr.Microphone() as  source:
    print("LISTENING....")
    voice=listener.listen(source)
    command=listener.recognize_google(voice)
    print(command)
    
        
        

