FROM python:3.10.5-alpine

RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir -p ./backend/site-media
RUN mkdir -p ./backend/db

COPY . /app
WORKDIR /app

COPY ./nginx/ssl /etc/ssl

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]