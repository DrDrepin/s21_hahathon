package minio

import (
	"fmt"
	"io"
	"log"
	"os"

	"github.com/minio/minio-go"
)

var minioClient *minio.Client

func Init() {
	var err error
	minioClient, err = minio.New("localhost:9000", "ozontech", "minio123", false)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Connecction established")
}

func CreateBucket(name string) {
	exists, err := minioClient.BucketExists(name)
	if err != nil || exists {
		fmt.Println(err)
		fmt.Println("Smth went wrong")

		return
	}
	errorus := minioClient.MakeBucket(name, "")
	if errorus != nil {
		fmt.Print(errorus)
	}
	fmt.Println("Bucket create")

}

func DownloadFile(name string, workspace string, path string) {
	uploadInfo, err := minioClient.FPutObject(workspace, name, path, minio.PutObjectOptions{})

	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(uploadInfo)
	return
}
func UploadFile(name string, workspace string, path string) {
	file, err := minioClient.GetObject(workspace, path+name, minio.GetObjectOptions{})
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()
	nw, errorus := os.Create("a/a/go.mod")
	if errorus != nil {
		fmt.Println("cant create file")
		return
	}
	defer nw.Close()
	if _, err := io.Copy(nw, file); err != nil {
		fmt.Println(err)
		return
	}
}
func DeleteFile(path string, workspace string) {
	err := minioClient.RemoveObject(workspace, path)
	if err != nil {
		fmt.Println(err)
	}

	return
}
