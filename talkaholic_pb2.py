# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: talkaholic.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='talkaholic.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10talkaholic.proto\"%\n\x11TalkaholicRequest\x12\x10\n\x08question\x18\x01 \x01(\t\"$\n\x12TalkaholicResponse\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\t2=\n\nTalkaholic\x12/\n\x04talk\x12\x12.TalkaholicRequest\x1a\x13.TalkaholicResponseb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TALKAHOLICREQUEST = _descriptor.Descriptor(
  name='TalkaholicRequest',
  full_name='TalkaholicRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='question', full_name='TalkaholicRequest.question', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=57,
)


_TALKAHOLICRESPONSE = _descriptor.Descriptor(
  name='TalkaholicResponse',
  full_name='TalkaholicResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='answer', full_name='TalkaholicResponse.answer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=95,
)

DESCRIPTOR.message_types_by_name['TalkaholicRequest'] = _TALKAHOLICREQUEST
DESCRIPTOR.message_types_by_name['TalkaholicResponse'] = _TALKAHOLICRESPONSE

TalkaholicRequest = _reflection.GeneratedProtocolMessageType('TalkaholicRequest', (_message.Message,), dict(
  DESCRIPTOR = _TALKAHOLICREQUEST,
  __module__ = 'talkaholic_pb2'
  # @@protoc_insertion_point(class_scope:TalkaholicRequest)
  ))
_sym_db.RegisterMessage(TalkaholicRequest)

TalkaholicResponse = _reflection.GeneratedProtocolMessageType('TalkaholicResponse', (_message.Message,), dict(
  DESCRIPTOR = _TALKAHOLICRESPONSE,
  __module__ = 'talkaholic_pb2'
  # @@protoc_insertion_point(class_scope:TalkaholicResponse)
  ))
_sym_db.RegisterMessage(TalkaholicResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class TalkaholicStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.talk = channel.unary_unary(
          '/Talkaholic/talk',
          request_serializer=TalkaholicRequest.SerializeToString,
          response_deserializer=TalkaholicResponse.FromString,
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
            request_deserializer=TalkaholicRequest.FromString,
            response_serializer=TalkaholicResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Talkaholic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaTalkaholicServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def talk(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaTalkaholicStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def talk(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    talk.future = None


  def beta_create_Talkaholic_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('Talkaholic', 'talk'): TalkaholicRequest.FromString,
    }
    response_serializers = {
      ('Talkaholic', 'talk'): TalkaholicResponse.SerializeToString,
    }
    method_implementations = {
      ('Talkaholic', 'talk'): face_utilities.unary_unary_inline(servicer.talk),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Talkaholic_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('Talkaholic', 'talk'): TalkaholicRequest.SerializeToString,
    }
    response_deserializers = {
      ('Talkaholic', 'talk'): TalkaholicResponse.FromString,
    }
    cardinalities = {
      'talk': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'Talkaholic', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
