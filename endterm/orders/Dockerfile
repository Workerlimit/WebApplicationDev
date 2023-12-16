FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN pip install Flask-Migrate
ENV FLASK_APP orders.py

RUN flask db init && flask db migrate && flask db upgrade   

EXPOSE 5002

ENV NAME OrdersMicroservice

CMD ["python", "orders.py"]
