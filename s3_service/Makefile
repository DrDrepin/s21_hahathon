NAME = golang

all : build

build :
	bash build_go.sh
	docker build . --tag $(NAME)

run : build
	docker run -d -p 8785:8785 $(NAME)
