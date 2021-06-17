FROM python:3.8.6-slim-buster

COPY api /app
COPY requirements.txt /requirements.txt
COPY models /models

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -c 'import nltk; nltk.download("punkt")'
RUN python -c 'import nltk; nltk.download("stopwords")'
RUN python -c 'import nltk; nltk.download("popular")'

#CMD tail -f /dev/null
CMD uvicorn app.fast:app --host 0.0.0.0 --port $PORT