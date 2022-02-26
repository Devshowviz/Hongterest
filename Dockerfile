FROM python:3.9.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/Devshowviz/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=django-insecure-$cfw)k6xn(v(2c)@qn3x0qylv^5g*3ew_zor9z=&k24c^vplt!" > .env

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]