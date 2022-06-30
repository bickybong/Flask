FROM python: 3.6.1-alpine

RUN pip install --upgrade pip

WORKDIR /FLASK

ADD . /FLASK

RUN pip install -r requirements.txt

CMD ["python", "app.py"]