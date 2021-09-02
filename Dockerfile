FROM python:3.7.9

WORKDIR \AsyncApi

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python3 main.py