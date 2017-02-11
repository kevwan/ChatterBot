from chatterbot import ChatBot

chatbot = ChatBot(
    'bot@liao',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter='chatterbot.adapters.storage.MongoDatabaseAdapter',
    database="chatterbot-100k"
)

# Get a response to an input statement
while True:
    content = input("> ")
    if content == "exit":
        break
    resp = chatbot.get_response(content)
    print(resp)
