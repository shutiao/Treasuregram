FROM python:latest

#RUN apt-get updatei \
#    apt-get install -y --no-install-recommends \
#    postgresql-client \

WORKDIR /usr/src/tryDjango
COPY requirements.txt ./
RUN pip install -r requirements.txt
#COPY ..

EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0:8000"]

