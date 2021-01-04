FROM python:3.7.7-alpine3.11

WORKDIR /delve
ADD . /delve/

ENV PORT=8000

RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE $PORT
CMD ./entrypoint.sh $PORT
