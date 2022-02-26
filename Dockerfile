FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/Devshowviz/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-$cfw)k6xn(v(2c)@qn3x0qylv^5g*3ew_zor9z=&k24c^vplt!" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]