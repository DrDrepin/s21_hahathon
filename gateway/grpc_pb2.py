# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngrpc.proto\x12\x0ctransmission\"\x18\n\x06\x42inary\x12\x0e\n\x06\x62inary\x18\x02 \x01(\x0c\"\x14\n\x04Path\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x18\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\x08\"c\n\x08SendFile\x12,\n\x10path_to_new_file\x18\x01 \x01(\x0b\x32\x12.transmission.Path\x12)\n\x0b\x62inary_file\x18\x02 \x01(\x0b\x32\x14.transmission.Binary\"u\n\x08TakeFile\x12.\n\x0b\x62inary_file\x18\x01 \x01(\x0b\x32\x14.transmission.BinaryH\x00\x88\x01\x01\x12)\n\x0b\x62ool_status\x18\x02 \x01(\x0b\x32\x14.transmission.StatusB\x0e\n\x0c_binary_file2\xd8\x01\n\x0cTransmission\x12\x42\n\x10SendFileToServer\x12\x16.transmission.SendFile\x1a\x14.transmission.Status\"\x00\x12\x42\n\x12TakeFileFromServer\x12\x12.transmission.Path\x1a\x16.transmission.TakeFile\"\x00\x12@\n\x12\x44\x65leteFileOnServer\x12\x12.transmission.Path\x1a\x14.transmission.Status\"\x00\x42\x11Z\x0f./minio-serviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\017./minio-service'
  _globals['_BINARY']._serialized_start=28
  _globals['_BINARY']._serialized_end=52
  _globals['_PATH']._serialized_start=54
  _globals['_PATH']._serialized_end=74
  _globals['_STATUS']._serialized_start=76
  _globals['_STATUS']._serialized_end=100
  _globals['_SENDFILE']._serialized_start=102
  _globals['_SENDFILE']._serialized_end=201
  _globals['_TAKEFILE']._serialized_start=203
  _globals['_TAKEFILE']._serialized_end=320
  _globals['_TRANSMISSION']._serialized_start=323
  _globals['_TRANSMISSION']._serialized_end=539
# @@protoc_insertion_point(module_scope)