FROM golang:latest
WORKDIR /build/golang
COPY . /build/golang
EXPOSE 80
RUN go mod tidy
CMD go run main.go
