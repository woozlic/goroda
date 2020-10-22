# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='helloworld.proto',
  package='helloworld',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10helloworld.proto\x12\nhelloworld\"*\n\x0cLobbyRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"+\n\nLobbyReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\"\x1c\n\x0cLoginRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nLoginReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1c\n\tIPRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"\x1a\n\x07IPReply\x12\x0f\n\x07message\x18\x01 \x01(\t\":\n\x0e\x43ommandRequest\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x0e\n\x06letter\x18\x02 \x01(\t\x12\x0b\n\x03pid\x18\x03 \x01(\t\"8\n\x0c\x43ommandReply\x12\x0b\n\x03msg\x18\x01 \x01(\t\x12\x0e\n\x06letter\x18\x02 \x01(\t\x12\x0b\n\x03pid\x18\x03 \x01(\t2\xfa\x01\n\x07Greeter\x12;\n\x05Login\x12\x18.helloworld.LoginRequest\x1a\x16.helloworld.LoginReply\"\x00\x12\x32\n\x02IP\x12\x15.helloworld.IPRequest\x1a\x13.helloworld.IPReply\"\x00\x12\x41\n\x07\x43ommand\x12\x1a.helloworld.CommandRequest\x1a\x18.helloworld.CommandReply\"\x00\x12;\n\x05Lobby\x12\x18.helloworld.LobbyRequest\x1a\x16.helloworld.LobbyReply\"\x00\x62\x06proto3'
)




_LOBBYREQUEST = _descriptor.Descriptor(
  name='LobbyRequest',
  full_name='helloworld.LobbyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='helloworld.LobbyRequest.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='helloworld.LobbyRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=74,
)


_LOBBYREPLY = _descriptor.Descriptor(
  name='LobbyReply',
  full_name='helloworld.LobbyReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='helloworld.LobbyReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='helloworld.LobbyReply.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=119,
)


_LOGINREQUEST = _descriptor.Descriptor(
  name='LoginRequest',
  full_name='helloworld.LoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='helloworld.LoginRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=149,
)


_LOGINREPLY = _descriptor.Descriptor(
  name='LoginReply',
  full_name='helloworld.LoginReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='helloworld.LoginReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=180,
)


_IPREQUEST = _descriptor.Descriptor(
  name='IPRequest',
  full_name='helloworld.IPRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='helloworld.IPRequest.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=210,
)


_IPREPLY = _descriptor.Descriptor(
  name='IPReply',
  full_name='helloworld.IPReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='helloworld.IPReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=238,
)


_COMMANDREQUEST = _descriptor.Descriptor(
  name='CommandRequest',
  full_name='helloworld.CommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='helloworld.CommandRequest.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='letter', full_name='helloworld.CommandRequest.letter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pid', full_name='helloworld.CommandRequest.pid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=298,
)


_COMMANDREPLY = _descriptor.Descriptor(
  name='CommandReply',
  full_name='helloworld.CommandReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='helloworld.CommandReply.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='letter', full_name='helloworld.CommandReply.letter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pid', full_name='helloworld.CommandReply.pid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=356,
)

DESCRIPTOR.message_types_by_name['LobbyRequest'] = _LOBBYREQUEST
DESCRIPTOR.message_types_by_name['LobbyReply'] = _LOBBYREPLY
DESCRIPTOR.message_types_by_name['LoginRequest'] = _LOGINREQUEST
DESCRIPTOR.message_types_by_name['LoginReply'] = _LOGINREPLY
DESCRIPTOR.message_types_by_name['IPRequest'] = _IPREQUEST
DESCRIPTOR.message_types_by_name['IPReply'] = _IPREPLY
DESCRIPTOR.message_types_by_name['CommandRequest'] = _COMMANDREQUEST
DESCRIPTOR.message_types_by_name['CommandReply'] = _COMMANDREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LobbyRequest = _reflection.GeneratedProtocolMessageType('LobbyRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOBBYREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.LobbyRequest)
  })
_sym_db.RegisterMessage(LobbyRequest)

LobbyReply = _reflection.GeneratedProtocolMessageType('LobbyReply', (_message.Message,), {
  'DESCRIPTOR' : _LOBBYREPLY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.LobbyReply)
  })
_sym_db.RegisterMessage(LobbyReply)

LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

LoginReply = _reflection.GeneratedProtocolMessageType('LoginReply', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREPLY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.LoginReply)
  })
_sym_db.RegisterMessage(LoginReply)

IPRequest = _reflection.GeneratedProtocolMessageType('IPRequest', (_message.Message,), {
  'DESCRIPTOR' : _IPREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.IPRequest)
  })
_sym_db.RegisterMessage(IPRequest)

IPReply = _reflection.GeneratedProtocolMessageType('IPReply', (_message.Message,), {
  'DESCRIPTOR' : _IPREPLY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.IPReply)
  })
_sym_db.RegisterMessage(IPReply)

CommandRequest = _reflection.GeneratedProtocolMessageType('CommandRequest', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.CommandRequest)
  })
_sym_db.RegisterMessage(CommandRequest)

CommandReply = _reflection.GeneratedProtocolMessageType('CommandReply', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDREPLY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.CommandReply)
  })
_sym_db.RegisterMessage(CommandReply)



_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='helloworld.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=359,
  serialized_end=609,
  methods=[
  _descriptor.MethodDescriptor(
    name='Login',
    full_name='helloworld.Greeter.Login',
    index=0,
    containing_service=None,
    input_type=_LOGINREQUEST,
    output_type=_LOGINREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='IP',
    full_name='helloworld.Greeter.IP',
    index=1,
    containing_service=None,
    input_type=_IPREQUEST,
    output_type=_IPREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Command',
    full_name='helloworld.Greeter.Command',
    index=2,
    containing_service=None,
    input_type=_COMMANDREQUEST,
    output_type=_COMMANDREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Lobby',
    full_name='helloworld.Greeter.Lobby',
    index=3,
    containing_service=None,
    input_type=_LOBBYREQUEST,
    output_type=_LOBBYREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
