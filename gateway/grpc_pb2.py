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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngrpc.proto\x12\x0ctransmission\"9\n\x05\x66iles\x12!\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x12.transmission.File\x12\r\n\x05total\x18\x02 \x01(\x05\"c\n\x04User\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\r\n\x05login\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\tB\x05\n\x03_id\"@\n\tWorkspace\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\tB\x05\n\x03_id\"C\n\rWorkspaceFile\x12\x14\n\x0cworkspace_id\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0e\n\x06\x62uffer\x18\x03 \x01(\x0c\"b\n\x04\x46ile\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x03 \x01(\t\x12\x13\n\x06\x62uffer\x18\x04 \x01(\x0cH\x01\x88\x01\x01\x42\x05\n\x03_idB\t\n\x07_buffer\"D\n\x06\x46older\x12\x0f\n\x02id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x03 \x01(\tB\x05\n\x03_id\"\x18\n\x06\x42inary\x12\x0e\n\x06\x62inary\x18\x02 \x01(\x0c\"\x14\n\x04Path\x12\x0c\n\x04path\x18\x01 \x01(\t\"\x18\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\x08\"c\n\x08SendFile\x12,\n\x10path_to_new_file\x18\x01 \x01(\x0b\x32\x12.transmission.Path\x12)\n\x0b\x62inary_file\x18\x02 \x01(\x0b\x32\x14.transmission.Binary\"u\n\x08TakeFile\x12.\n\x0b\x62inary_file\x18\x01 \x01(\x0b\x32\x14.transmission.BinaryH\x00\x88\x01\x01\x12)\n\x0b\x62ool_status\x18\x02 \x01(\x0b\x32\x14.transmission.StatusB\x0e\n\x0c_binary_file2\xe0\x04\n\x0cTransmission\x12\x36\n\nCreateUser\x12\x12.transmission.User\x1a\x12.transmission.User\"\x00\x12\x36\n\nUpdateUser\x12\x12.transmission.User\x1a\x12.transmission.User\"\x00\x12\x34\n\x08ReadUser\x12\x12.transmission.User\x1a\x12.transmission.User\"\x00\x12\x42\n\x0f\x43reateWorkspace\x12\x17.transmission.Workspace\x1a\x14.transmission.Status\"\x00\x12\x38\n\nCreateFile\x12\x12.transmission.File\x1a\x14.transmission.Status\"\x00\x12<\n\x07GetFile\x12\x1b.transmission.WorkspaceFile\x1a\x12.transmission.File\"\x00\x12\x38\n\nDeleteFile\x12\x12.transmission.File\x1a\x14.transmission.Status\"\x00\x12<\n\x0c\x43reateFolder\x12\x14.transmission.Folder\x1a\x14.transmission.Status\"\x00\x12\x38\n\tGetFolder\x12\x14.transmission.Folder\x1a\x13.transmission.files\"\x00\x12<\n\x0c\x44\x65leteFolder\x12\x14.transmission.Folder\x1a\x14.transmission.Status\"\x00\x42\x11Z\x0f./minio-serviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\017./minio-service'
  _globals['_FILES']._serialized_start=28
  _globals['_FILES']._serialized_end=85
  _globals['_USER']._serialized_start=87
  _globals['_USER']._serialized_end=186
  _globals['_WORKSPACE']._serialized_start=188
  _globals['_WORKSPACE']._serialized_end=252
  _globals['_WORKSPACEFILE']._serialized_start=254
  _globals['_WORKSPACEFILE']._serialized_end=321
  _globals['_FILE']._serialized_start=323
  _globals['_FILE']._serialized_end=421
  _globals['_FOLDER']._serialized_start=423
  _globals['_FOLDER']._serialized_end=491
  _globals['_BINARY']._serialized_start=493
  _globals['_BINARY']._serialized_end=517
  _globals['_PATH']._serialized_start=519
  _globals['_PATH']._serialized_end=539
  _globals['_STATUS']._serialized_start=541
  _globals['_STATUS']._serialized_end=565
  _globals['_SENDFILE']._serialized_start=567
  _globals['_SENDFILE']._serialized_end=666
  _globals['_TAKEFILE']._serialized_start=668
  _globals['_TAKEFILE']._serialized_end=785
  _globals['_TRANSMISSION']._serialized_start=788
  _globals['_TRANSMISSION']._serialized_end=1396
# @@protoc_insertion_point(module_scope)
