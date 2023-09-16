// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             v3.20.3
// source: transmission/transmission.proto

package minio_service

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

const (
	Transmission_SendFileToServer_FullMethodName   = "/transmission.Transmission/SendFileToServer"
	Transmission_TakeFileFromServer_FullMethodName = "/transmission.Transmission/TakeFileFromServer"
	Transmission_DeleteFileOnServer_FullMethodName = "/transmission.Transmission/DeleteFileOnServer"
)

// TransmissionClient is the client API for Transmission service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TransmissionClient interface {
	SendFileToServer(ctx context.Context, in *SendFile, opts ...grpc.CallOption) (*Status, error)
	TakeFileFromServer(ctx context.Context, in *Path, opts ...grpc.CallOption) (*TakeFile, error)
	DeleteFileOnServer(ctx context.Context, in *Path, opts ...grpc.CallOption) (*Status, error)
}

type transmissionClient struct {
	cc grpc.ClientConnInterface
}

func NewTransmissionClient(cc grpc.ClientConnInterface) TransmissionClient {
	return &transmissionClient{cc}
}

func (c *transmissionClient) SendFileToServer(ctx context.Context, in *SendFile, opts ...grpc.CallOption) (*Status, error) {
	out := new(Status)
	err := c.cc.Invoke(ctx, Transmission_SendFileToServer_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transmissionClient) TakeFileFromServer(ctx context.Context, in *Path, opts ...grpc.CallOption) (*TakeFile, error) {
	out := new(TakeFile)
	err := c.cc.Invoke(ctx, Transmission_TakeFileFromServer_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transmissionClient) DeleteFileOnServer(ctx context.Context, in *Path, opts ...grpc.CallOption) (*Status, error) {
	out := new(Status)
	err := c.cc.Invoke(ctx, Transmission_DeleteFileOnServer_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TransmissionServer is the server API for Transmission service.
// All implementations must embed UnimplementedTransmissionServer
// for forward compatibility
type TransmissionServer interface {
	SendFileToServer(context.Context, *SendFile) (*Status, error)
	TakeFileFromServer(context.Context, *Path) (*TakeFile, error)
	DeleteFileOnServer(context.Context, *Path) (*Status, error)
	mustEmbedUnimplementedTransmissionServer()
}

// UnimplementedTransmissionServer must be embedded to have forward compatible implementations.
type UnimplementedTransmissionServer struct {
}

func (UnimplementedTransmissionServer) SendFileToServer(context.Context, *SendFile) (*Status, error) {
	return nil, status.Errorf(codes.Unimplemented, "method SendFileToServer not implemented")
}
func (UnimplementedTransmissionServer) TakeFileFromServer(context.Context, *Path) (*TakeFile, error) {
	return nil, status.Errorf(codes.Unimplemented, "method TakeFileFromServer not implemented")
}
func (UnimplementedTransmissionServer) DeleteFileOnServer(context.Context, *Path) (*Status, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteFileOnServer not implemented")
}
func (UnimplementedTransmissionServer) mustEmbedUnimplementedTransmissionServer() {}

// UnsafeTransmissionServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to TransmissionServer will
// result in compilation errors.
type UnsafeTransmissionServer interface {
	mustEmbedUnimplementedTransmissionServer()
}

func RegisterTransmissionServer(s grpc.ServiceRegistrar, srv TransmissionServer) {
	s.RegisterService(&Transmission_ServiceDesc, srv)
}

func _Transmission_SendFileToServer_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(SendFile)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransmissionServer).SendFileToServer(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Transmission_SendFileToServer_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransmissionServer).SendFileToServer(ctx, req.(*SendFile))
	}
	return interceptor(ctx, in, info, handler)
}

func _Transmission_TakeFileFromServer_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Path)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransmissionServer).TakeFileFromServer(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Transmission_TakeFileFromServer_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransmissionServer).TakeFileFromServer(ctx, req.(*Path))
	}
	return interceptor(ctx, in, info, handler)
}

func _Transmission_DeleteFileOnServer_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Path)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransmissionServer).DeleteFileOnServer(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Transmission_DeleteFileOnServer_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransmissionServer).DeleteFileOnServer(ctx, req.(*Path))
	}
	return interceptor(ctx, in, info, handler)
}

// Transmission_ServiceDesc is the grpc.ServiceDesc for Transmission service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Transmission_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "transmission.Transmission",
	HandlerType: (*TransmissionServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "SendFileToServer",
			Handler:    _Transmission_SendFileToServer_Handler,
		},
		{
			MethodName: "TakeFileFromServer",
			Handler:    _Transmission_TakeFileFromServer_Handler,
		},
		{
			MethodName: "DeleteFileOnServer",
			Handler:    _Transmission_DeleteFileOnServer_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "transmission/transmission.proto",
}