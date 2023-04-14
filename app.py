from dotenv import load_dotenv
import os
import openai
import pyttsx3
import speech_recognition as sr

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')  # supply your API key however you choose
engine = pyttsx3.init()
r = sr.Recognizer()


def diz_p_user(pergunta):
    """Essa funçao lê a resposta da API para o usuario."""
    engine.setProperty('age', 10)
    engine.setProperty('voice', 'brazil')
    engine.setProperty('rate', 200)
    engine.say(pergunta)
    engine.runAndWait()



def gpt_msg(mensagem):
    """Essa Função faz o request na API da openai e aciona a funçao 'diz_p_user'."""
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=[{"role": "user", "content": f"{mensagem}"}])
    diz_p_user(completion.choices[0].message.content)


while True:  # Loop principal do app
    with sr.Microphone() as source:  # utiliza o mic do usuario
        print("Para fazer uma busca ao chat gpt diga 'OLA GPT' e a pergunta logo em seguida")
        audio = r.listen(source)

    try:
        if "Olá GPT" in r.recognize_google(audio, language='pt-BR'):  # Se o usuario falar 'Ola GPT' o texto transcrito
            gpt_msg(r.recognize_google(audio, language='pt-BR'))  # da fala do usuario é encaminhado para api do openai
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o áudio")
    except sr.RequestError as e:
        print("Erro ao requisitar o serviço de reconhecimento de fala; {0}".format(e))