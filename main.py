### Importing necessary libraries

import configparser         # pip install configparser
from telethon import TelegramClient, events         # pip install telethon
from datetime import datetime
import MySQLdb      # pip install mysqlclient

### Initializing Configuration
print("Initializing configuration...")
config = configparser.ConfigParser()
config.read('config.ini')

# Read values for Telethon and set session name
API_ID = config.get('default','api_id') 
API_HASH = config.get('default','api_hash')
BOT_TOKEN = config.get('default','bot_token')
session_name = "sessions/Bot"

# Read values for MySQLdb
HOSTNAME = config.get('default','hostname')
USERNAME = config.get('default','username')
PASSWORD = config.get('default','password')
DATABASE = config.get('default','database')
 
# Start the Client (telethon)
client = TelegramClient(session_name, API_ID, API_HASH).start(bot_token=BOT_TOKEN)


### START COMMAND
@client.on(events.NewMessage(pattern="(?i)/start"))
async def start(event):
    # Get sender
    sender = await event.get_sender()
    SENDER = sender.id
    
    # set text and send message
    text = "Olá, sou o Bot de ajuda com quedas de energia em Roraima.🤖💡\nEm que posso ajudar ?"
    await client.send_message(SENDER, text)


### Insert command
# @client.on(events.NewMessage(pattern="(?i)/insert"))
# async def insert(event):
#     try:
#         # Get the sender of the message
#         sender = await event.get_sender()
#         SENDER = sender.id

#         # /insert BoaVista JardimFloresta 23-06-02

#         # Get the text of the user AFTER the /insert command and convert it to a list (we are splitting by the SPACE " " simbol)
#         list_of_words = event.message.text.split(" ")
#         cidade = list_of_words[1] 
#         local = list_of_words[2] 
#         dia = datetime.now().strftime("%Y/%m/%d") 

#         # Create the tuple "params" with all the parameters inserted by the user
#         params = (cidade, local, dia)
#         sql_command = "INSERT INTO manutencao VALUES (NULL, %s, %s, %s);" # the initial NULL is for the AUTOINCREMENT id inside the table
#         crsr.execute(sql_command, params) # Execute the query
#         conn.commit() # commit the changes

#         # If at least 1 row is affected by the query we send specific messages
#         if crsr.rowcount < 1:
#             text = "Alguma coisa deu errado. Por favor tente outra vez.\nPara inserir segue o exemplo (/insert BoaVista JardimFloresta 23-06-02)"
#             await client.send_message(SENDER, text, parse_mode='html')
#         else:
#             text = "Manutencao inserida corretamente"
#             await client.send_message(SENDER, text, parse_mode='html')

#     except Exception as e: 
#         print(e)
#         await client.send_message(SENDER, "Algo de errado aconteceu... Verifique seu código!", parse_mode='html')
#         return

# Function that creates a message containing a list of all the oders
def create_message_select_query(ans):
    text = ""
    for i in ans:
        cidade = i[1]
        local = i[2]
        dia = i[3]
        text += "<b>"+ str(cidade) +"</b> | " + "<b>"+ str(local)+"</b> | " + "<b>"+ str(dia)+"</b>\n\n"
    message = "<b>Recebido📖\n</b>Informações sobre Falta de energia em Roraima:\n\n"+text
    return message

@client.on(events.NewMessage(pattern="(?i)/energia"))
async def opcoes(event):
    # Get sender
    sender = await event.get_sender()
    SENDER = sender.id
    
    # set text and send message
    text = "Certo, Digite a opção que você deseja ver ?\n/boavista\n/saoluiz\n/caracarai\n/tudo"
    await client.send_message(SENDER, text)

### SELECT COMMAND
@client.on(events.NewMessage(pattern="(?i)/tudo"))
async def select(event):
    try:
        # Get the sender of the message
        sender = await event.get_sender()
        SENDER = sender.id
        # Execute the query and get all (*) the oders
        crsr.execute("SELECT * FROM manutencao")
        res = crsr.fetchall() # fetch all the results
        # If there is at least 1 row selected, print a message with the list of all the oders
        # The message is created using the function defined above
        if(res):
            text = create_message_select_query(res) 
            await client.send_message(SENDER, text, parse_mode='html')
        # Otherwhise, print a default text
        else:
            text = "Nenhuma manutencao encontrada dentro do banco de dados."
            await client.send_message(SENDER, text, parse_mode='html')

    except Exception as e: 
        print(e)
        await client.send_message(SENDER, "Algo de errado aconteceu... Verifique seu código!", parse_mode='html')
        return

@client.on(events.NewMessage(pattern="(?i)/boavista"))
async def boavista(event):
    try:
        # Get the sender of the message
        sender = await event.get_sender()
        SENDER = sender.id
        # Execute the query and get all (*) the oders
        crsr.execute("SELECT * FROM `manutencao` WHERE cidade = 'Boa Vista'")
        res = crsr.fetchall() # fetch all the results
        # If there is at least 1 row selected, print a message with the list of all the oders
        # The message is created using the function defined above
        if(res):
            text = create_message_select_query(res) 
            await client.send_message(SENDER, text, parse_mode='html')
        # Otherwhise, print a default text
        else:
            text = "Nenhuma manutencao encontrada dentro do banco de dados."
            await client.send_message(SENDER, text, parse_mode='html')

    except Exception as e: 
        print(e)
        await client.send_message(SENDER, "Algo de errado aconteceu... Verifique seu código!", parse_mode='html')
        return

@client.on(events.NewMessage(pattern="(?i)/saoluiz"))
async def boavista(event):
    try:
        # Get the sender of the message
        sender = await event.get_sender()
        SENDER = sender.id
        # Execute the query and get all (*) the oders
        crsr.execute("SELECT * FROM `manutencao` WHERE cidade = 'São Luiz'")
        res = crsr.fetchall() # fetch all the results
        # If there is at least 1 row selected, print a message with the list of all the oders
        # The message is created using the function defined above
        if(res):
            text = create_message_select_query(res) 
            await client.send_message(SENDER, text, parse_mode='html')
        # Otherwhise, print a default text
        else:
            text = "Nenhuma manutencao encontrada dentro do banco de dados."
            await client.send_message(SENDER, text, parse_mode='html')

    except Exception as e: 
        print(e)
        await client.send_message(SENDER, "Algo de errado aconteceu... Verifique seu código!", parse_mode='html')
        return

@client.on(events.NewMessage(pattern="(?i)/caracarai"))
async def boavista(event):
    try:
        # Get the sender of the message
        sender = await event.get_sender()
        SENDER = sender.id
        # Execute the query and get all (*) the oders
        crsr.execute("SELECT * FROM `manutencao` WHERE cidade = 'Caracaraí'")
        res = crsr.fetchall() # fetch all the results
        # If there is at least 1 row selected, print a message with the list of all the oders
        # The message is created using the function defined above
        if(res):
            text = create_message_select_query(res) 
            await client.send_message(SENDER, text, parse_mode='html')
        # Otherwhise, print a default text
        else:
            text = "Nenhuma manutencao encontrada dentro do banco de dados."
            await client.send_message(SENDER, text, parse_mode='html')

    except Exception as e: 
        print(e)
        await client.send_message(SENDER, "Algo de errado aconteceu... Verifique seu código!", parse_mode='html')
        return


# Create database function
# def create_database(query):
#     try:
#         crsr_mysql.execute(query)
#         print("Database created successfully")
#     except Exception as e:
#         print(f"WARNING: '{e}'")

##### MAIN
if __name__ == '__main__':
    try:
        print("Initializing Database...")
        # conn_mysql = MySQLdb.connect( host=HOSTNAME, user=USERNAME, passwd=PASSWORD )
        # crsr_mysql = conn_mysql.cursor()

        # query = "CREATE DATABASE "+str(DATABASE)
        # create_database(query)
        conn = MySQLdb.connect( host=HOSTNAME, user=USERNAME, passwd=PASSWORD, db=DATABASE )
        crsr = conn.cursor()

        # Command that creates the "manutencao" table 
        # sql_command = """CREATE TABLE IF NOT EXISTS manutencao ( 
        #     id INTEGER PRIMARY KEY AUTO_INCREMENT, 
        #     product VARCHAR(200),
        #     quantity INT(10), 
        #     LAST_EDIT VARCHAR(100));"""

        # crsr.execute(sql_command)
        # print("All tables are ready")
        
        print("Bot Started...")
        client.run_until_disconnected()

    except Exception as error:
        print('Cause: {}'.format(error))