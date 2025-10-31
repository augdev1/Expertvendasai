import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print('Diga seu comando:')
    audio = recognizer.listen(source)
    comando = recognizer.recognize_google(audio, language='pt-BR')
    print('Você disse:', comando)
    
