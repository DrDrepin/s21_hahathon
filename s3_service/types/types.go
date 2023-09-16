package types

type File struct {
	Name   string  `json:name`
	Buffer []uint8 `json:data`
}

type FetchFilesResponse struct {
	Files []File `json:files`
}

type UploadFileModel struct {
	Id        string         `json:id`
	Name      string         `json:name`
	Workspace WorkspaceModel `json:workspace`
}

type DownloadFileModel struct {
	Id        string         `json:id`
	Name      string         `json:name`
	Workspace WorkspaceModel `json:workspace`
}

type WorkspaceModel struct {
	id   string `json:id`
	name string `json:name`
}

type FetchFilesRequest struct {
	Filenames []string `json:filenames`
}
