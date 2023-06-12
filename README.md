## Integrantes: Lucas Prado Ribeiro e Marcos Vinicius Melo
## Chatbot-Telegram-Docker
Este Projeto fornece uma implementação em Python de um Telegram Chatbot para informações de quedas de energia baseado no modelo OpenAI GPT-3. Este bot usa a biblioteca Telethon do Python3 MTProto para interagir com a API Telegram Bot e a API OpenAI para gerar respostas às consultas do usuário, conectado com um banco de dados MySQL e uma interface Phpmyadmin para administração do MySQL, cada aplicação dentro de um container Docker separado e conectados em uma mesma rede para uma arquitetura dividida em microsserviços.  

## Microsserviços 


## Executando o Projeto
1. Para começar, certifique-se de ter o Docker instalado em sua máquina: https://docs.docker.com/get-docker/

2. Clone este repositório para o seu computador

3. Altere o arquivo **`config.ini`** com seus valores:

    -> APP_ID e API_HASH para o telethon: https://my.telegram.org/auth

    -> BOT_TOKEN: Escreva no telegram para @BotFather e siga as instruções

    -> openai_key: Sua chave de API OpenAI https://platform.openai.com/account/api-keys

4. Em seguida, navegue até a pasta do projeto e execute o seguinte comando para criar as imagens do Docker: `docker-compose build`.

5. Para executar o contêiner do Docker, use o seguinte comando: `docker-compose up`

6. Depois que o contêiner estiver em execução, acesse o Telegram e envie o comando /start para o seu bot.
