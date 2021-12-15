FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install flask_sqlalchemy
RUN pip3 install flask_marshmallow 
RUN pip3 install marshmallow-sqlalchemy

ENTRYPOINT ["python3"]
CMD ["app.py"]
