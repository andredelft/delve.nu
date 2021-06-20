FROM python:3.7.7-alpine3.11

ENV PORT=8000
EXPOSE $PORT

ADD requirements.txt /

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /

CMD ./entrypoint.sh $PORT
