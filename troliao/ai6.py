import speech_recognition
hear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	question='Hãy ra lệnh bằng giọng nói !...'
	print(question)
	audio = hear.listen(mic)
	you = hear.recognize_google(audio,language="vi-VI")
	print(you)
