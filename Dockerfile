FROM python:3.12.2-alpine
LABEL authors="citroncorp@mail.ru"
LABEL maintainers="citroncorp@mail.ru"
WORKDIR /usr/src/libreforms
COPY . .
RUN apk update && apk add gcc python3-dev musl-dev && apk add postgresql-dev
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python", "./manage.py", "runserver"]
