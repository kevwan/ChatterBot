import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import talkaholic_pb2 as talkaholic__pb2
import talkaholic_pb2 as talkaholic__pb2


class TalkaholicStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.talk = channel.unary_unary(
        '/Talkaholic/talk',
        request_serializer=talkaholic__pb2.TalkaholicRequest.SerializeToString,
        response_deserializer=talkaholic__pb2.TalkaholicResponse.FromString,
        )


class TalkaholicServicer(object):

  def talk(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TalkaholicServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'talk': grpc.unary_unary_rpc_method_handler(
          servicer.talk,
          request_deserializer=talkaholic__pb2.TalkaholicRequest.FromString,
          response_serializer=talkaholic__pb2.TalkaholicResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Talkaholic', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
