# ChatGPT-por-voz
Esse é um script em Python que utiliza a API da OpenAI, a biblioteca pyttsx3 para text-to-speech (texto para fala) e a biblioteca speech_recognition para reconhecimento de fala. O objetivo é criar um chatbot que possa interagir com o usuário através de voz.

O script começa importando as bibliotecas necessárias e carregando a chave de API da OpenAI a partir de um arquivo .env. Em seguida, inicializa o mecanismo de pyttsx3 e o reconhecedor de fala.

A função diz_p_user() é responsável por converter a resposta da API em fala para que o usuário possa ouvi-la. Ela usa o mecanismo pyttsx3 para reproduzir a mensagem fornecida como entrada.

A função gpt_msg() é responsável por enviar a pergunta do usuário para a API da OpenAI, receber a resposta e passá-la para a função diz_p_user() para que seja convertida em fala e ouvida pelo usuário.

Dentro do loop principal, o script espera que o usuário diga "Olá GPT" para começar a interagir com o chatbot. Quando o usuário diz "Olá GPT" seguido de uma pergunta, o texto da fala é transcrita e enviada para a função gpt_msg(), que envia a pergunta para a API da OpenAI e retorna a resposta para a função diz_p_user(), que converte a resposta em fala e a reproduz para o usuário.

Se ocorrer algum erro durante o processo de reconhecimento de fala ou na comunicação com a API da OpenAI, o script trata a exceção e exibe uma mensagem de erro.
