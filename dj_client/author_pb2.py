# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: author.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x61uthor.proto\x12\x06\x61uthor\"\x0f\n\rAuthorRequest\";\n\x0e\x41uthorResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07surname\x18\x03 \x01(\t2N\n\rAuthorService\x12=\n\nGetAuthors\x12\x15.author.AuthorRequest\x1a\x16.author.AuthorResponse0\x01\x62\x06proto3')



_AUTHORREQUEST = DESCRIPTOR.message_types_by_name['AuthorRequest']
_AUTHORRESPONSE = DESCRIPTOR.message_types_by_name['AuthorResponse']
AuthorRequest = _reflection.GeneratedProtocolMessageType('AuthorRequest', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORREQUEST,
  '__module__' : 'author_pb2'
  # @@protoc_insertion_point(class_scope:author.AuthorRequest)
  })
_sym_db.RegisterMessage(AuthorRequest)

AuthorResponse = _reflection.GeneratedProtocolMessageType('AuthorResponse', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORRESPONSE,
  '__module__' : 'author_pb2'
  # @@protoc_insertion_point(class_scope:author.AuthorResponse)
  })
_sym_db.RegisterMessage(AuthorResponse)

_AUTHORSERVICE = DESCRIPTOR.services_by_name['AuthorService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AUTHORREQUEST._serialized_start=24
  _AUTHORREQUEST._serialized_end=39
  _AUTHORRESPONSE._serialized_start=41
  _AUTHORRESPONSE._serialized_end=100
  _AUTHORSERVICE._serialized_start=102
  _AUTHORSERVICE._serialized_end=180
# @@protoc_insertion_point(module_scope)
