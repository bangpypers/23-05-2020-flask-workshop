FROM python:3.7-alpine

WORKDIR /flask-workshop

COPY ./requirements.txt /flask-workshop

RUN pip install -r requirements.txt

RUN pip install gunicorn

COPY . /flask-workshop

EXPOSE 5000

ENV FLASK_APP wsgi.py
RUN ["flask", "load-data", "movies.csv"]

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "wsgi:app"]
