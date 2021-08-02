FROM python:3.8

COPY ./Twitter Twitter

WORKDIR /Twitter

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD ["python","manage.py","runserver", "0.0.0.0:8000"]