from chatterbot import ChatBot

chatbot = ChatBot(
    'bot@liao',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter='chatterbot.adapters.storage.MongoDatabaseAdapter',
    database="chatterbot"
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.chinese.quarter")

# Get a response to an input statement
while True:
    content = input("> ")
    if content == "exit":
        break
    resp = chatbot.get_response(content)
    print(resp)
