// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.3.0
// - protoc             v3.20.3
// source: grpc.proto

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
	Transmission_CreateUser_FullMethodName      = "/transmission.Transmission/CreateUser"
	Transmission_UpdateUser_FullMethodName      = "/transmission.Transmission/UpdateUser"
	Transmission_ReadUser_FullMethodName        = "/transmission.Transmission/ReadUser"
	Transmission_CreateWorkspace_FullMethodName = "/transmission.Transmission/CreateWorkspace"
	Transmission_CreateFile_FullMethodName      = "/transmission.Transmission/CreateFile"
	Transmission_GetFile_FullMethodName         = "/transmission.Transmission/GetFile"
	Transmission_DeleteFile_FullMethodName      = "/transmission.Transmission/DeleteFile"
	Transmission_CreateFolder_FullMethodName    = "/transmission.Transmission/CreateFolder"
	Transmission_GetFolder_FullMethodName       = "/transmission.Transmission/GetFolder"
	Transmission_DeleteFolder_FullMethodName    = "/transmission.Transmission/DeleteFolder"
)

// TransmissionClient is the client API for Transmission service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type TransmissionClient interface {
	CreateUser(ctx context.Context, in *User, opts ...grpc.CallOption) (*User, error)
	UpdateUser(ctx context.Context, in *User, opts ...grpc.CallOption) (*User, error)
	ReadUser(ctx context.Context, in *User, opts ...grpc.CallOption) (*User, error)
	CreateWorkspace(ctx context.Context, in *Workspace, opts ...grpc.CallOption) (*Status, error)
	CreateFile(ctx context.Context, in *File, opts ...grpc.CallOption) (*Status, error)
	GetFile(ctx context.Context, in *WorkspaceFile, opts ...grpc.CallOption) (*File, error)
	DeleteFile(ctx context.Context, in *File, opts ...grpc.CallOption) (*Status, error)
	CreateFolder(ctx context.Context, in *Folder, opts ...grpc.CallOption) (*Status, error)
	GetFolder(ctx context.Context, in *Folder, opts ...grpc.CallOption) (*Files, error)
	DeleteFolder(ctx context.Context, in *Folder, opts ...grpc.CallOption) (*Status, error)
}

type transmissionClient struct {
	cc grpc.ClientConnInterface
}

func NewTransmissionClient(cc grpc.ClientConnInterface) TransmissionClient {
	return &transmissionClient{cc}
}

func (c *transmissionClient) CreateUser(ctx context.Context, in *User, opts ...grpc.CallOption) (*User, error) {
	out := new(User)
	err := c.cc.Invoke(ctx, Transmission_CreateUser_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transmissionClient) UpdateUser(ctx context.Context, in *User, opts ...grpc.CallOption) (*User, error) {
	out := new(User)
	err := c.cc.Invoke(ctx, Transmission_UpdateUser_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transmissionClient) ReadUser(ctx context.Context, in *User, opts ...grpc.CallOption) (*User, error) {
	out := new(User)
	err := c.cc.Invoke(ctx, Transmission_ReadUser_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transmissionClient) CreateWorkspace(ctx context.Context, in *Workspace, opts ...grpc.CallOption) (*Status, error) {
	out := new(Status)
	err := c.cc.Invoke(ctx, Transmission_CreateWorkspace_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transmissionClient) CreateFile(ctx context.Context, in *File, opts ...grpc.CallOption) (*Status, error) {
	out := new(Status)
	err := c.cc.Invoke(ctx, Transmission_CreateFile_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transmissionClient) GetFile(ctx context.Context, in *WorkspaceFile, opts ...grpc.CallOption) (*File, error) {
	out := new(File)
	err := c.cc.Invoke(ctx, Transmission_GetFile_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transmissionClient) DeleteFile(ctx context.Context, in *File, opts ...grpc.CallOption) (*Status, error) {
	out := new(Status)
	err := c.cc.Invoke(ctx, Transmission_DeleteFile_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transmissionClient) CreateFolder(ctx context.Context, in *Folder, opts ...grpc.CallOption) (*Status, error) {
	out := new(Status)
	err := c.cc.Invoke(ctx, Transmission_CreateFolder_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transmissionClient) GetFolder(ctx context.Context, in *Folder, opts ...grpc.CallOption) (*Files, error) {
	out := new(Files)
	err := c.cc.Invoke(ctx, Transmission_GetFolder_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *transmissionClient) DeleteFolder(ctx context.Context, in *Folder, opts ...grpc.CallOption) (*Status, error) {
	out := new(Status)
	err := c.cc.Invoke(ctx, Transmission_DeleteFolder_FullMethodName, in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// TransmissionServer is the server API for Transmission service.
// All implementations must embed UnimplementedTransmissionServer
// for forward compatibility
type TransmissionServer interface {
	CreateUser(context.Context, *User) (*User, error)
	UpdateUser(context.Context, *User) (*User, error)
	ReadUser(context.Context, *User) (*User, error)
	CreateWorkspace(context.Context, *Workspace) (*Status, error)
	CreateFile(context.Context, *File) (*Status, error)
	GetFile(context.Context, *WorkspaceFile) (*File, error)
	DeleteFile(context.Context, *File) (*Status, error)
	CreateFolder(context.Context, *Folder) (*Status, error)
	GetFolder(context.Context, *Folder) (*Files, error)
	DeleteFolder(context.Context, *Folder) (*Status, error)
	mustEmbedUnimplementedTransmissionServer()
}

// UnimplementedTransmissionServer must be embedded to have forward compatible implementations.
type UnimplementedTransmissionServer struct {
}

func (UnimplementedTransmissionServer) CreateUser(context.Context, *User) (*User, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateUser not implemented")
}
func (UnimplementedTransmissionServer) UpdateUser(context.Context, *User) (*User, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateUser not implemented")
}
func (UnimplementedTransmissionServer) ReadUser(context.Context, *User) (*User, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ReadUser not implemented")
}
func (UnimplementedTransmissionServer) CreateWorkspace(context.Context, *Workspace) (*Status, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateWorkspace not implemented")
}
func (UnimplementedTransmissionServer) CreateFile(context.Context, *File) (*Status, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateFile not implemented")
}
func (UnimplementedTransmissionServer) GetFile(context.Context, *WorkspaceFile) (*File, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetFile not implemented")
}
func (UnimplementedTransmissionServer) DeleteFile(context.Context, *File) (*Status, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteFile not implemented")
}
func (UnimplementedTransmissionServer) CreateFolder(context.Context, *Folder) (*Status, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateFolder not implemented")
}
func (UnimplementedTransmissionServer) GetFolder(context.Context, *Folder) (*Files, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetFolder not implemented")
}
func (UnimplementedTransmissionServer) DeleteFolder(context.Context, *Folder) (*Status, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteFolder not implemented")
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

func _Transmission_CreateUser_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(User)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransmissionServer).CreateUser(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Transmission_CreateUser_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransmissionServer).CreateUser(ctx, req.(*User))
	}
	return interceptor(ctx, in, info, handler)
}

func _Transmission_UpdateUser_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(User)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransmissionServer).UpdateUser(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Transmission_UpdateUser_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransmissionServer).UpdateUser(ctx, req.(*User))
	}
	return interceptor(ctx, in, info, handler)
}

func _Transmission_ReadUser_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(User)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransmissionServer).ReadUser(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Transmission_ReadUser_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransmissionServer).ReadUser(ctx, req.(*User))
	}
	return interceptor(ctx, in, info, handler)
}

func _Transmission_CreateWorkspace_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Workspace)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransmissionServer).CreateWorkspace(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Transmission_CreateWorkspace_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransmissionServer).CreateWorkspace(ctx, req.(*Workspace))
	}
	return interceptor(ctx, in, info, handler)
}

func _Transmission_CreateFile_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(File)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransmissionServer).CreateFile(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Transmission_CreateFile_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransmissionServer).CreateFile(ctx, req.(*File))
	}
	return interceptor(ctx, in, info, handler)
}

func _Transmission_GetFile_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(WorkspaceFile)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransmissionServer).GetFile(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Transmission_GetFile_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransmissionServer).GetFile(ctx, req.(*WorkspaceFile))
	}
	return interceptor(ctx, in, info, handler)
}

func _Transmission_DeleteFile_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(File)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransmissionServer).DeleteFile(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Transmission_DeleteFile_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransmissionServer).DeleteFile(ctx, req.(*File))
	}
	return interceptor(ctx, in, info, handler)
}

func _Transmission_CreateFolder_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Folder)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransmissionServer).CreateFolder(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Transmission_CreateFolder_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransmissionServer).CreateFolder(ctx, req.(*Folder))
	}
	return interceptor(ctx, in, info, handler)
}

func _Transmission_GetFolder_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Folder)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransmissionServer).GetFolder(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Transmission_GetFolder_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransmissionServer).GetFolder(ctx, req.(*Folder))
	}
	return interceptor(ctx, in, info, handler)
}

func _Transmission_DeleteFolder_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(Folder)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(TransmissionServer).DeleteFolder(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Transmission_DeleteFolder_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(TransmissionServer).DeleteFolder(ctx, req.(*Folder))
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
			MethodName: "CreateUser",
			Handler:    _Transmission_CreateUser_Handler,
		},
		{
			MethodName: "UpdateUser",
			Handler:    _Transmission_UpdateUser_Handler,
		},
		{
			MethodName: "ReadUser",
			Handler:    _Transmission_ReadUser_Handler,
		},
		{
			MethodName: "CreateWorkspace",
			Handler:    _Transmission_CreateWorkspace_Handler,
		},
		{
			MethodName: "CreateFile",
			Handler:    _Transmission_CreateFile_Handler,
		},
		{
			MethodName: "GetFile",
			Handler:    _Transmission_GetFile_Handler,
		},
		{
			MethodName: "DeleteFile",
			Handler:    _Transmission_DeleteFile_Handler,
		},
		{
			MethodName: "CreateFolder",
			Handler:    _Transmission_CreateFolder_Handler,
		},
		{
			MethodName: "GetFolder",
			Handler:    _Transmission_GetFolder_Handler,
		},
		{
			MethodName: "DeleteFolder",
			Handler:    _Transmission_DeleteFolder_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "grpc.proto",
}
