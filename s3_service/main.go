package main

import (
	"context"
	"fmt"
	minio_service "hahaton/grpc/transmission"
	"hahaton/minio"
	"log"
	"net"
	"os"
	"os/signal"

	"google.golang.org/grpc"
)

type server struct {
	minio_service.TransmissionServer
}

func (s *server) SendFileToServer(ctx context.Context, req *minio_service.SendFile) (*minio_service.Status, error) {
	return &minio_service.Status{
		Status: true,
	}, nil
}
func (s *server) TakeFileFromServer(ctx context.Context, req *minio_service.Path) (*minio_service.TakeFile, error) {
	return &minio_service.TakeFile{
		BoolStatus: &minio_service.Status{
			Status: true,
		},
		BinaryFile: &minio_service.Binary{
			Binary: make([][]byte, 0),
		},
	}, nil
}
func (s *server) DeleteFileOnServer(ctx context.Context, req *minio_service.Path) (*minio_service.Status, error) {
	return &minio_service.Status{
		Status: true,
	}, nil
}

func main() {

	minio.Init()

	lis, err := net.Listen("tcp", "localhost:8785")

	if err != nil {
		log.Fatal(err)
	}
	var opts []grpc.ServerOption
	s := grpc.NewServer(opts...)

	minio_service.RegisterTransmissionServer(s, &server{})
	go func() {
		fmt.Println("Starting Server...")
		if err := s.Serve(lis); err != nil {
			log.Fatalf("failed to serve: %v", err)
		}
	}()

	// Wait for Control C to exit
	ch := make(chan os.Signal, 1)
	signal.Notify(ch, os.Interrupt)

	// Block until a signal is received
	<-ch
	fmt.Println("Goodbye")

	s.Stop()

}
