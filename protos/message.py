# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import objects


DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='',
  serialized_pb=_b('\n\rmessage.proto\x1a\robjects.proto\"\x8b\x01\n\x07Message\x12\x11\n\tmessageID\x18\x01 \x02(\x0c\x12\x15\n\x06sender\x18\x02 \x02(\x0b\x32\x05.Node\x12\x19\n\x07\x63ommand\x18\x03 \x02(\x0e\x32\x08.Command\x12\x10\n\x08protoVer\x18\x04 \x02(\r\x12\x11\n\targuments\x18\x05 \x03(\x0c\x12\x16\n\x07testnet\x18\x06 \x01(\x08:\x05\x66\x61lse*\xfd\x03\n\x07\x43ommand\x12\x08\n\x04PING\x10\x01\x12\x08\n\x04STUN\x10\x02\x12\x0e\n\nHOLE_PUNCH\x10\x03\x12\t\n\x05STORE\x10\x04\x12\n\n\x06\x44\x45LETE\x10\x05\x12\x07\n\x03INV\x10\x06\x12\n\n\x06VALUES\x10\x07\x12\r\n\tBROADCAST\x10\x08\x12\x0b\n\x07MESSAGE\x10\t\x12\n\n\x06\x46OLLOW\x10\n\x12\x0c\n\x08UNFOLLOW\x10\x0b\x12\t\n\x05ORDER\x10\x0c\x12\x16\n\x12ORDER_CONFIRMATION\x10\r\x12\x12\n\x0e\x43OMPLETE_ORDER\x10\x0e\x12\r\n\tFIND_NODE\x10\x0f\x12\x0e\n\nFIND_VALUE\x10\x10\x12\x10\n\x0cGET_CONTRACT\x10\x11\x12\r\n\tGET_IMAGE\x10\x12\x12\x0f\n\x0bGET_PROFILE\x10\x13\x12\x10\n\x0cGET_LISTINGS\x10\x14\x12\x15\n\x11GET_USER_METADATA\x10\x15\x12\x19\n\x15GET_CONTRACT_METADATA\x10\x16\x12\x11\n\rGET_FOLLOWING\x10\x17\x12\x11\n\rGET_FOLLOWERS\x10\x18\x12\x0f\n\x0bGET_RATINGS\x10\x19\x12\x10\n\x0c\x44ISPUTE_OPEN\x10\x1a\x12\x11\n\rDISPUTE_CLOSE\x10\x1b\x12\x10\n\x0b\x42\x41\x44_REQUEST\x10\x90\x03\x12\x0e\n\tNOT_FOUND\x10\x94\x03\x12\x0e\n\tCALM_DOWN\x10\xa4\x03\x12\x12\n\rUNKNOWN_ERROR\x10\x88\x04')
  ,
  dependencies=[objects.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_COMMAND = _descriptor.EnumDescriptor(
  name='Command',
  full_name='Command',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PING', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STUN', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOLE_PUNCH', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INV', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUES', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BROADCAST', index=7, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MESSAGE', index=8, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOLLOW', index=9, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNFOLLOW', index=10, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER', index=11, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER_CONFIRMATION', index=12, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE_ORDER', index=13, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIND_NODE', index=14, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIND_VALUE', index=15, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_CONTRACT', index=16, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_IMAGE', index=17, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_PROFILE', index=18, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_LISTINGS', index=19, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_USER_METADATA', index=20, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_CONTRACT_METADATA', index=21, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_FOLLOWING', index=22, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_FOLLOWERS', index=23, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_RATINGS', index=24, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISPUTE_OPEN', index=25, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISPUTE_CLOSE', index=26, number=27,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_REQUEST', index=27, number=400,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=28, number=404,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CALM_DOWN', index=29, number=420,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ERROR', index=30, number=520,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=175,
  serialized_end=684,
)
_sym_db.RegisterEnumDescriptor(_COMMAND)

Command = enum_type_wrapper.EnumTypeWrapper(_COMMAND)
PING = 1
STUN = 2
HOLE_PUNCH = 3
STORE = 4
DELETE = 5
INV = 6
VALUES = 7
BROADCAST = 8
MESSAGE = 9
FOLLOW = 10
UNFOLLOW = 11
ORDER = 12
ORDER_CONFIRMATION = 13
COMPLETE_ORDER = 14
FIND_NODE = 15
FIND_VALUE = 16
GET_CONTRACT = 17
GET_IMAGE = 18
GET_PROFILE = 19
GET_LISTINGS = 20
GET_USER_METADATA = 21
GET_CONTRACT_METADATA = 22
GET_FOLLOWING = 23
GET_FOLLOWERS = 24
GET_RATINGS = 25
DISPUTE_OPEN = 26
DISPUTE_CLOSE = 27
BAD_REQUEST = 400
NOT_FOUND = 404
CALM_DOWN = 420
UNKNOWN_ERROR = 520



_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messageID', full_name='Message.messageID', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sender', full_name='Message.sender', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command', full_name='Message.command', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protoVer', full_name='Message.protoVer', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arguments', full_name='Message.arguments', index=4,
      number=5, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='testnet', full_name='Message.testnet', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=172,
)

_MESSAGE.fields_by_name['sender'].message_type = objects._NODE
_MESSAGE.fields_by_name['command'].enum_type = _COMMAND
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.enum_types_by_name['Command'] = _COMMAND

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  ))
_sym_db.RegisterMessage(Message)


# @@protoc_insertion_point(module_scope)
