import grpc
import signal
from concurrent import futures
import talkaholic_pb2, talkaholic_pb2_grpc
from chatterbot import ChatBot


chatbot = ChatBot(
    'bot@liao',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter='chatterbot.adapters.storage.MongoDatabaseAdapter',
    database="chatterbot-100k"
)


class TalkaholicServicer(talkaholic_pb2_grpc.TalkaholicServicer):
    def talk(self, request, context):
        resp = chatbot.get_response(request.question)
        return talkaholic_pb2.TalkaholicResponse(answer=resp.text)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
talkaholic_pb2_grpc.add_TalkaholicServicer_to_server(TalkaholicServicer(), server)
server.add_insecure_port(":9400")
server.start()

try:
    signal.pause()
except KeyboardInterrupt:
    pass

