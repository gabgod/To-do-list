FROM python:3.13.0a4-alpine3.19

WORKDIR /code

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt



COPY ./api ./api

COPY ./todolist ./todolist

COPY ./manage.py ./manage.py

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver","0.0.0.0:8000" ]

