FROM python:3.9.21-alpine3.21

WORKDIR /app

COPY . .

RUN pip install -r ./requirements.txt

CMD [ "python", "app.py" ]
