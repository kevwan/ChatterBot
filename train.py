from chatterbot import ChatBot

chatbot = ChatBot(
    'bot@liao',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter='chatterbot.adapters.storage.MongoDatabaseAdapter',
    database="chatterbot-20k"
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.chinese.20k")
