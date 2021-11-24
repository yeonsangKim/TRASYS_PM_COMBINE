FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/yeonsangKim/TRASYS_PM_COMBINE.git

WORKDIR /home/PM_combine_

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-764q=$_of#a7!3&0f^_qqlhploz-b^gxcptjcj8dbw%5()67)p" > .env


RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]