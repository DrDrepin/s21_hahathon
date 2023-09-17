all : build run

build :
	bash generate.sh

run : build
	source venv/bin/activate && uvicorn main:app --reload --port 9999

open :
	open http://127.0.0.1:9999/docs

clean :
	rm -rf venv __pycache__