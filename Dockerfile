FROM python:3.8-alpine

WORKDIR /src

RUN apk add --no-cache gcc musl-dev linux-headers curl

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000