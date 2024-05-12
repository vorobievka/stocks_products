Dockerfile
    FROM python:3.8-alpine
    WORKDIR /src
    RUN apk add --no-cache gcc musl-dev linux-headers curl
    COPY ./requirements.txt ./requirements.txt
    RUN pip install --no-cache-dir --upgrade -r requirements.txt
    COPY . .
    EXPOSE 8000
    RUN python manage.py migrate
    CMD python manage.py runserver 0.0.0.0:8000

Собрать Docker Image с помощью команды
    docker build -t stocks_products .

Запустить контейнер командой
    docker run --name stocks_products -d -p 8000:8000 stocks_products
