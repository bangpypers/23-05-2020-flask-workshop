FROM python:3.7-alpine

WORKDIR /flask-workshop

COPY ./requirements.txt /flask-workshop

RUN pip install -r requirements.txt

RUN pip install gunicorn

COPY . /flask-workshop

CMD ["gunicorn", "-w", "4", "wsgi:app"]
