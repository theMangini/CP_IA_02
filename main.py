import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import time
#import smtplib
#import os
#from sklearn.cluster import spectral_clustering
#from voice import microphone




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)#Escolher a voz para falar português ou inglês, sendo 0 português e 1 Inglês
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Sim, mestre. O que posso fazer?")
        speak("Aproveitando, Bom dia! Seja bem vindo")

    elif hour >= 12 and hour < 18:
        speak("Sim, mestre. O que posso fazer?")
        speak("Aproveitando, Boa tarde! Seja bem vindo")

    else:
        speak("Sim, mestre. O que posso fazer?")
        speak("Aproveitando, Boa noite! Seja bem vindo")



def takeCommand():
    #It takes mocrophones input from the user and returns string output
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ouvindo...")
        r.pause_threshold = 1
        audio = r.listen(source)
        #validar o problema
    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language='pt-BR')
        print(f"Usuário disse: {query}\n")
    except Exception as e:
        #print(e)
        print("Pode repetir, por favor...")
        return "None"
    return query

def save_event(evento):
    se = open('Evento.txt', 'a')
    se.writelines(evento + '\n')
    time.sleep(3)
    speak("Evento criado, mais algum desejo, mestre?")
    

def read_event():
    re = open('Evento.txt', 'r')
    return re.read()

speak("Para avançar Diga a palavra mágica: ")
query = takeCommand().lower()

if 'ok sexta-feira' in query:
    takeCommand()
    if __name__ == "__main__":
        wishMe()
        time.sleep(2)
        while 'sair' not in query:
            query = takeCommand().lower()
            if 'wikipédia' in query:
                speak('Pesquisando na Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("De acordo com a Wikipedia")
                print(results)
                speak(results)
            
            elif 'abrir youtube' in query:
                webbrowser.open("youtube.com")
                speak("Youtube aberto, mestre")
                
            elif "falar data e hora" in query:
                data = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M")
                speak(data, + ", mais algum desejo, mestre?")
                
            elif 'quero escutar uma música' in query:
                webbrowser.open("https://www.youtube.com/watch?v=f2D2hEFnHLU")
                speak("Vou te mostrar o que é musica de verdade, essa é do balácu bácu")
                
            elif 'como está o clima' in query:
                webbrowser.open("https://www.google.com.br/search?q=como+está+o+clima&sxsrf=ALiCzsa6DVaueTjPzd-AImhYp2iz-SX1Ag%3A1652941478953&ei=puKFYqPoOYna1sQPyuWS6A4&ved=0ahUKEwij07_t9ur3AhUJrZUCHcqyBO0Q4dUDCA0&uact=5&oq=como+está+o+clima&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQgAIyCAgAEIAEEMkDMggIABCxAxCDATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjELADECc6BwgAEEcQsAM6CgguEMcBENEDECc6BAgjECc6CwgAEIAEELEDEIMBOgsILhCABBCxAxCDAToUCC4QgAQQsQMQgwEQxwEQowIQ1AI6DgguEIAEELEDEMcBEKMCOggILhCxAxCDAToLCC4QgAQQxwEQowI6BAguEEM6BAgAEEM6EQguEIAEELEDEMcBEKMCENQCOg4ILhCABBCxAxCDARDUAjoICAAQgAQQsQM6BQgAEJIDOgUILhCABDoECAAQAzoQCAAQgAQQsQMQgwEQRhCAAkoECEEYAEoECEYYAFC9BVj9JGC9KGgBcAF4AIABjgGIAasQkgEEMC4xN5gBAKABAcgBCcABAQ&sclient=gws-wiz")
                speak("Aqui estão as informações do clima.")
                
            elif 'cadastrar evento na agenda' in query:
                speak("Ok, qual evento devo cadastrar?")
                print("Escrevendo...")
                
                
            elif 'abrir stack overflow' in query:
                webbrowser.open("stackoverflow.com")
                
            elif 'criar um evento' in query:
                #speak('Qual evento devo cadastrar, mestre?')
                #save_event(microphone()) 
                
                speak("Ok, qual evento devo cadastrar?")
                print("Ok, qual evento devo cadastrar?")
                query = takeCommand().lower()
                save_event(query)  
                             
            elif 'ler agenda' in query:
                print("Lendo agenda")
                speak(read_event())
            
            



#https://acervolima.com/assistente-de-voz-usando-python/




