FROM python:3.8
WORKDIR /docker_work
RUN pip install nltk
RUN python -m nltk.downloader stopwords punkt
COPY paragraphs.txt .
COPY ass.py .
CMD python ass.py
