FROM python:latest
WORKDIR /build/python
COPY . /build/python
EXPOSE 9999
RUN bash generate.sh && . venv/bin/activate
CMD uvicorn main:app --reload --port 9999
