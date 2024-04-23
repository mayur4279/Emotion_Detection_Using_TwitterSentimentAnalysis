FROM python:latest  

RUN apt-get update -y  

RUN apt-get upgrade -y  

RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"

RUN pip install --upgrade pip

WORKDIR /usr/src/app

COPY . .   

RUN pip install Django  

RUN pip install numpy 

RUN pip install textblob  

RUN pip install tweepy

RUN pip install pandas 

EXPOSE 8000  

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



