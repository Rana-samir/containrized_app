FROM python:latest
WORKDIR /docker_work
RUN pip install nltk
COPY ass.py .
CMD python ass.py