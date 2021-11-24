FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/yeonsangKim/TRASYS_PM_COMBINE.git

WORKDIR /home/TRASYS_PM_COMBINE/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-41#^*v+ohezq@)*he0um!hb+rne--8syq**zf)k0bt##k8$4)9" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD=["python","manage.py","runserver","0.0.0.0:8000"]