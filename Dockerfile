FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/philjoong/graffiti.git

WORKDIR /home/graffitie/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-1mnd_h+^(ho#3ns5j=&nlpp!ifx6k8-c-#^@8yk(p2&j&-i^r7" > .env

RUN python manage.py migrate

EXPOSE 9000

CMD["python", "manage.py", "runserver", "0.0.0.0:8000"]
