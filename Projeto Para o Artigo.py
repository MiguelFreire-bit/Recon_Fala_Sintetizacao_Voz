import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import time



def FuncaoQueIraRepetir():
    en.setProperty('voice', b'brazil')
    en.setProperty('rate', 200)
    en.setProperty('volume', 1)
    en.runAndWait()

def FuncaodeRetorno():
    en.say("Olá, em que mais posso ajudar?")
    FuncaoQueIraRepetir()

def Funcaoprincipal(x):
    if x == "voltar para o início":
        en.say("ok!")
        FuncaoQueIraRepetir()
        time.sleep(2)
        FuncaodeRetorno()

    elif x == "desejo Abrir o Google":
        en.say("Ok, abrindo o google!")
        FuncaoQueIraRepetir()
        webbrowser.open('https://www.google.com/')
        time.sleep(3)
        FuncaodeRetorno()

    elif x == "Abra o YouTube":
        en.say("Ok, abrindo o youtube!")
        webbrowser.open('https://www.youtube.com/?gl=BR&hl=pt')
        FuncaoQueIraRepetir()
        time.sleep(3)
        FuncaodeRetorno()

    elif x == "encerra o programa":
        en.say("Ok, encerrando a aplicação")
        FuncaoQueIraRepetir()


    else:
        en.say('Desculpe, não foi possível compreender sua solicitação')
        FuncaoQueIraRepetir()
        FuncaodeRetorno()

def FuncaoMusica():
    en.say("Qual música deseja ouvir, Miguel")
    FuncaoQueIraRepetir()
    if FuncaoQueFala() == "Sonic":
        en.say("ok, Tocando Sonic.")
        FuncaoQueIraRepetir()
        os.system('8d82b5_Sonic_Marble_Zone_Theme_Song.mp3')
        time.sleep(5)
    else:
        en.say("Desculpe, não foi possível compreender sua solicitação")
        FuncaoQueIraRepetir()

def FuncaoQueFala():
    fala = reconhecimento.listen(source)
    y = reconhecimento.recognize_google(fala, language='pt')
    return y



verificador = str()
en = pyttsx3.init()
en.say("Olá, Miguel, Como posso lhe auxiliar?")
FuncaoQueIraRepetir()
reconhecimento = sr.Recognizer()

with sr.Microphone() as source:
    while verificador != "encerra o programa":
        audio = reconhecimento.listen(source)
        resposta = reconhecimento.recognize_google(audio, language='pt')
        verificador = resposta
        if resposta == "desejo ouvir uma música":
            FuncaoMusica()
            FuncaodeRetorno()
            audio = reconhecimento.listen(source)
            resposta = reconhecimento.recognize_google(audio, language='pt')
        Funcaoprincipal(resposta)
