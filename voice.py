import speech_recognition as sr

def microphone():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print('Fale')
        audio = rec.listen(source, timeout= 5, phrase_time_limit= 10)
        translate_audio = rec.recognize_google(audio, language = "pt-br")

        return translate_audio