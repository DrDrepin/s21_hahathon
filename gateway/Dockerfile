FROM python:latest
WORKDIR /build/python
COPY . /build/python
EXPOSE 9999
RUN bash generate.sh && source venv/bin/activate && uvicorn main:app --reload --port 9999
CMD python3 main.py
