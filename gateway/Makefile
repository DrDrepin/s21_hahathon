UNAME = $(shell uname -s)

ifeq ($(UNAME), Linux)
	CMD = .
else
	CMD = source
endif


all : build run

build :
	bash generate.sh

run : build
	$(CMD) venv/bin/activate && uvicorn main:app --reload --port 9999

open :
	open http://127.0.0.1:9999/docs

clean :
	rm -rf venv __pycache__
