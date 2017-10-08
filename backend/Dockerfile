FROM python:3.6
ENV PYTHONUNBUFFERED 1

COPY ./backend/requirements.txt /app/backend/requirements.txt

WORKDIR /app/backend
RUN pip install -r requirements.txt

COPY ./backend/manage.py /app/backend/manage.py
COPY ./backend/api/      /app/backend/api/
COPY ./backend/backend/  /app/backend/backend/

CMD python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000