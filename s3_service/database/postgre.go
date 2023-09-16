package database

import (
	"database/sql"
	"hahaton/minio"
	minio_service "hahaton/minio-service"
	"hahaton/types"
	"log"
	"strings"

	_ "github.com/lib/pq"
)

var myPostgres *sql.DB

func Init() error {
	connStr := "user=postgres password=postgres dbname=postgres sslmode=disable"

	var err error
	myPostgres, err = sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}
	myPostgres.Exec(`create table if not exist workspaces(
		id uuid not null default gen_random_uuid(),
		name character varying not null,
	);`)
	myPostgres.Exec(`create table if not exist users(
		id uuid not null default gen_random_uuid(),
		login character varying not null,
		password character varying not null,
		workspace_id uuid not null,
		role character varying
	);`)
	myPostgres.Exec(`create table if not exist files(
		id uuid not null default gen_random_uuid(),
		path character varying not null unique,
		parent_id uuid,
		workspace_id uuid not null,
	);`)
	myPostgres.Exec(`create table if not exist folders(
		id uuid not null default gen_random_uuid(),
		path character varying not null,
		parent_id uuid,
		workspace_id uuid not null,
	);`)
	return err
}

func CreateDBUser(user minio_service.User) minio_service.User {
	_, err := myPostgres.Exec("insert into users values(default,$1,$2,$3,$4);", user.Login, user.Password, user.WorkspaceId, user.Role)
	if err != nil {
		log.Fatal(err)
		return user
	}
	return user
}

func UpdateUser(user minio_service.User) minio_service.User {
	_, err := myPostgres.Exec("insert into users values(default,$1,$2,$3,$4);", user.Login, user.Password, user.WorkspaceId, user.Role)
	if err != nil {
		log.Fatal(err)
		return user
	}
	return user
}

func ReadUser(user minio_service.User) minio_service.User {
	_, err := myPostgres.Exec("select * from users where login = $1 and password = $2 and workspace_id;", user.Login, user.Password, user.WorkspaceId)
	if err != nil {
		log.Fatal(err)
		return user
	}
	return user
}

func CreateBucket(workspace minio_service.Workspace) minio_service.Status {
	minio.CreateBucket(workspace.Name)
	return minio_service.Status{
		Status: true,
	}
}

func CreateFolder(folder minio_service.Folder) minio_service.Status {
	_, err := myPostgres.Exec("insert into folders values(default,$1,$2);", folder.Path, folder.WorkspaceId)
	var status minio_service.Status
	status.Status = true
	if err != nil {
		status.Status = false
	}
	return status
}
func GetFolder(folder minio_service.Folder) minio_service.Status {
	_, err := myPostgres.Exec("select * from folders where path like('$1') and path not like('$2/%');", folder.Path, folder.WorkspaceId)
	var status minio_service.Status
	status.Status = true
	if err != nil {
		status.Status = false
	}
	return status
}
func DeleteFolder(folder minio_service.Folder) minio_service.Status {
	_, err := myPostgres.Exec("delete from folders where path = '$1' and workspace_id = '$2';", folder.Path, folder.WorkspaceId)
	var status minio_service.Status
	status.Status = true
	if err != nil {
		status.Status = false
	}
	return status
}

func CreateFile(file minio_service.File) minio_service.Status {
	path := strings.Split(file.Path, "/")
	var status minio_service.Status

	var newPath string
	for i := 0; i < len(path)-2; i++ {
		newPath = "/" + path[i]
	}
	res, err := myPostgres.Query("select * from folders where path = '$1' and workspace_id= '$2';", newPath, file.WorkspaceId)
	if err != nil {
		status.Status = false
		return status
	}
	defer res.Close()

	var fold types.UploadFileModel
	scanErr := res.Scan(&fold)
	if scanErr != nil {
		status.Status = false

		return status
	}
	_, inErr := myPostgres.Exec("insert into files values(default,$1,$2,$3);", file.Path, fold.Id, file.WorkspaceId)
	status.Status = true
	if inErr != nil {
		status.Status = false
	}
	return status
}
func GetFile(path string, workspace string) string {
	scan, err := myPostgres.Query("select * from files where path = '$1' and workspace_id = '$2';", path, workspace)
	var status minio_service.Status
	status.Status = true
	if err != nil {
		status.Status = false
	}
	defer scan.Close()
	var f *minio_service.File
	scan.Scan(f)
	if f == nil {
		return ""
	}
	return f.Path
}

func DeleteFile() bool {

	return true

}
