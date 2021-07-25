import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    while True:
        audio=r.listen(source,timeout=2,phrase_time_limit=5)
        try:
            text=r.recognize_google(audio)
            print(text)
            if text=="hello":
            	print("chao ban nhe")
        except:
            print('sorry')
        os.system("cls")