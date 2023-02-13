FROM python:3.8

COPY requirements.txt /opt/
RUN pip3 install -r /opt/requirements.txt

WORKDIR /opt
COPY . /opt/
EXPOSE 5000
ENV FLASK_APP=app
ENV FLASK_DEBUG=1
CMD  ["python", "app.py"]