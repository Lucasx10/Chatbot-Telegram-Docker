import re
import openai
import configparser
from telethon import TelegramClient, events
from datetime import datetime
import MySQLdb

# Initializing Configuration
print("Initializing configuration...")
config = configparser.ConfigParser()
config.read('config.ini')

# Read values for Telethon and set session name
API_ID = config.get('default', 'api_id')
API_HASH = config.get('default', 'api_hash')
BOT_TOKEN = config.get('default', 'bot_token')
API_KEY = config.get('openai', 'api_key')
session_name = "sessions/Bot"

# Read values for MySQLdb
HOSTNAME = config.get('default', 'hostname')
USERNAME = config.get('default', 'username')
PASSWORD = config.get('default', 'password')
DATABASE = config.get('default', 'database')

# Start the Client (telethon)
client = TelegramClient(session_name, API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# OpenAI API configuration
openai.api_key = API_KEY

# MySQL database connection
conn = MySQLdb.connect(host=HOSTNAME, user=USERNAME, passwd=PASSWORD, db=DATABASE)
crsr = conn.cursor()

# Function that creates a message containing a list of all the orders
def create_message_select_query(ans):
    text = ""
    for i in ans:
        cidade = i[1]
        local = i[2]
        motivo = i[3]
        dia = i[4]
        text += "<b>"+ str(cidade) +"</b> | " + "<b>"+ str(local)+"</b> | " + "<b>"+ str(motivo)+"</b>\n" + "<b>"+ str(dia)+"</b>\n\n"
    message = "<b>Recebido📖\n</b>Informações sobre Falta de energia em Roraima:\n\n"+text
    return message

# Function to handle user messages
@client.on(events.NewMessage)
async def handle_message(event):
    # Get sender
    sender = await event.get_sender()
    SENDER = sender.id
    
    # Get user's message
    user_message = event.message.text.lower()
    
    # Check if user's message is "/start"
    if user_message == "/start":
        # Send the introductory message
        intro_message = "Olá! Eu sou um bot de informações sobre falta de enrgia em Roraima🤖💡. Atualmente consigo disponibilizar informações sobre 3 cidades do estado, sendo eles:\n \n</b>- Boa Vista</b>\n</b>- São Luiz</b>\n</b>- Caracaraí</b> \n \n Lembrando que sou só um bot sobre quedas de energia, só me faça perguntas relacionadas ao assunto 😁"
        await client.send_message(SENDER, intro_message, parse_mode='html')
    elif re.search(r'\bboa vista\b', user_message):
        try:
            # Execute the query and get all (*) the orders
            crsr.execute("SELECT * FROM `manutencao` WHERE cidade = 'Boa Vista'")
            res = crsr.fetchall()  # fetch all the results
            
            if res:
                # Create a message with the list of orders
                text = create_message_select_query(res)
                await client.send_message(SENDER, text, parse_mode='html')
            else:
                text = "Nenhuma manutencao encontrada dentro do banco de dados."
                await client.send_message(SENDER, text, parse_mode='html')
        except Exception as e:
            print(e)
            await client.send_message(SENDER, "Algo de errado aconteceu... Verifique seu código!", parse_mode='html')
            return
    elif re.search(r'\bsão luiz\b', user_message):
        try:
            # Execute the query and get all (*) the orders
            crsr.execute("SELECT * FROM `manutencao` WHERE cidade = 'São Luiz'")
            res = crsr.fetchall()  # fetch all the results
            
            if res:
                # Create a message with the list of orders
                text = create_message_select_query(res)
                await client.send_message(SENDER, text, parse_mode='html')
            else:
                text = "Nenhuma manutencao encontrada dentro do banco de dados."
                await client.send_message(SENDER, text, parse_mode='html')
        except Exception as e:
            print(e)
            await client.send_message(SENDER, "Algo de errado aconteceu... Verifique seu código!", parse_mode='html')
            return
    elif re.search(r'\bcaracaraí\b', user_message):
        try:
            # Execute the query and get all (*) the orders
            crsr.execute("SELECT * FROM `manutencao` WHERE cidade = 'Caracaraí'")
            res = crsr.fetchall()  # fetch all the results
            
            if res:
                # Create a message with the list of orders
                text = create_message_select_query(res)
                await client.send_message(SENDER, text, parse_mode='html')
            else:
                text = "Nenhuma manutencao encontrada dentro do banco de dados."
                await client.send_message(SENDER, text, parse_mode='html')
        except Exception as e:
            print(e)
            await client.send_message(SENDER, "Algo de errado aconteceu... Verifique seu código!", parse_mode='html')
            return
    elif re.search(r'\bobrigado\b', user_message):
        # Generate the response using OpenAI
        prompt = "obrigado"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7
        )
        answer = response.choices[0].text.strip()
        
        # Send the response to the user
        await client.send_message(SENDER, answer)
    else:
        # Send the introductory message
        intro_message = "Desculpe, mas não consigo responder isso, porém aqui vão algumas informações sobre as quedas de energia em Roraima:"
        await client.send_message(SENDER, intro_message)
        
        # Prompt engineering: Add additional information to the question or context
        prompt = "mensagem curta sobre as Quedas de energia em Roraima:\n"
        
        # Generate response from OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7
        )
        answer = response.choices[0].text.strip()
        
        # Send the response to the user
        await client.send_message(SENDER, answer)


# Main program
if __name__ == '__main__':
    print("Bot is running...")
    client.run_until_disconnected()