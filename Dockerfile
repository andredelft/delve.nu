FROM python:3.7.7-alpine3.11

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /

ENV PORT=8000

EXPOSE $PORT
CMD ./entrypoint.sh $PORT
