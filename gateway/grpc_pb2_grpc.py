# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_pb2 as grpc__pb2


class TransmissionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/transmission.Transmission/CreateUser',
                request_serializer=grpc__pb2.User.SerializeToString,
                response_deserializer=grpc__pb2.User.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/transmission.Transmission/UpdateUser',
                request_serializer=grpc__pb2.User.SerializeToString,
                response_deserializer=grpc__pb2.User.FromString,
                )
        self.ReadUser = channel.unary_unary(
                '/transmission.Transmission/ReadUser',
                request_serializer=grpc__pb2.User.SerializeToString,
                response_deserializer=grpc__pb2.User.FromString,
                )
        self.CreateWorkspace = channel.unary_unary(
                '/transmission.Transmission/CreateWorkspace',
                request_serializer=grpc__pb2.Workspace.SerializeToString,
                response_deserializer=grpc__pb2.Status.FromString,
                )
        self.CreateFile = channel.unary_unary(
                '/transmission.Transmission/CreateFile',
                request_serializer=grpc__pb2.File.SerializeToString,
                response_deserializer=grpc__pb2.Status.FromString,
                )
        self.GetFile = channel.unary_unary(
                '/transmission.Transmission/GetFile',
                request_serializer=grpc__pb2.WorkspaceFile.SerializeToString,
                response_deserializer=grpc__pb2.File.FromString,
                )
        self.DeleteFile = channel.unary_unary(
                '/transmission.Transmission/DeleteFile',
                request_serializer=grpc__pb2.File.SerializeToString,
                response_deserializer=grpc__pb2.Status.FromString,
                )
        self.CreateFolder = channel.unary_unary(
                '/transmission.Transmission/CreateFolder',
                request_serializer=grpc__pb2.Folder.SerializeToString,
                response_deserializer=grpc__pb2.Status.FromString,
                )
        self.GetFolder = channel.unary_unary(
                '/transmission.Transmission/GetFolder',
                request_serializer=grpc__pb2.Folder.SerializeToString,
                response_deserializer=grpc__pb2.files.FromString,
                )
        self.DeleteFolder = channel.unary_unary(
                '/transmission.Transmission/DeleteFolder',
                request_serializer=grpc__pb2.Folder.SerializeToString,
                response_deserializer=grpc__pb2.Status.FromString,
                )


class TransmissionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateWorkspace(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFolder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFolder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFolder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransmissionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=grpc__pb2.User.FromString,
                    response_serializer=grpc__pb2.User.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=grpc__pb2.User.FromString,
                    response_serializer=grpc__pb2.User.SerializeToString,
            ),
            'ReadUser': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadUser,
                    request_deserializer=grpc__pb2.User.FromString,
                    response_serializer=grpc__pb2.User.SerializeToString,
            ),
            'CreateWorkspace': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateWorkspace,
                    request_deserializer=grpc__pb2.Workspace.FromString,
                    response_serializer=grpc__pb2.Status.SerializeToString,
            ),
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=grpc__pb2.File.FromString,
                    response_serializer=grpc__pb2.Status.SerializeToString,
            ),
            'GetFile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFile,
                    request_deserializer=grpc__pb2.WorkspaceFile.FromString,
                    response_serializer=grpc__pb2.File.SerializeToString,
            ),
            'DeleteFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFile,
                    request_deserializer=grpc__pb2.File.FromString,
                    response_serializer=grpc__pb2.Status.SerializeToString,
            ),
            'CreateFolder': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFolder,
                    request_deserializer=grpc__pb2.Folder.FromString,
                    response_serializer=grpc__pb2.Status.SerializeToString,
            ),
            'GetFolder': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFolder,
                    request_deserializer=grpc__pb2.Folder.FromString,
                    response_serializer=grpc__pb2.files.SerializeToString,
            ),
            'DeleteFolder': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFolder,
                    request_deserializer=grpc__pb2.Folder.FromString,
                    response_serializer=grpc__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'transmission.Transmission', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Transmission(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transmission.Transmission/CreateUser',
            grpc__pb2.User.SerializeToString,
            grpc__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transmission.Transmission/UpdateUser',
            grpc__pb2.User.SerializeToString,
            grpc__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transmission.Transmission/ReadUser',
            grpc__pb2.User.SerializeToString,
            grpc__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateWorkspace(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transmission.Transmission/CreateWorkspace',
            grpc__pb2.Workspace.SerializeToString,
            grpc__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transmission.Transmission/CreateFile',
            grpc__pb2.File.SerializeToString,
            grpc__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transmission.Transmission/GetFile',
            grpc__pb2.WorkspaceFile.SerializeToString,
            grpc__pb2.File.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transmission.Transmission/DeleteFile',
            grpc__pb2.File.SerializeToString,
            grpc__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateFolder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transmission.Transmission/CreateFolder',
            grpc__pb2.Folder.SerializeToString,
            grpc__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFolder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transmission.Transmission/GetFolder',
            grpc__pb2.Folder.SerializeToString,
            grpc__pb2.files.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteFolder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/transmission.Transmission/DeleteFolder',
            grpc__pb2.Folder.SerializeToString,
            grpc__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)