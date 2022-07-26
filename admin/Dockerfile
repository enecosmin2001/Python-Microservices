FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE admin.settings
WORKDIR /app 

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt 

COPY . /app