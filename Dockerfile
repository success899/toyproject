FROM python:3.9.0

WORKDIR /home/

RUN echo "testing8"

RUN git clone https://github.com/success899/toyproject.git

WORKDIR /home/toyproject/

RUN pip install -r requirements.txt

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=toyproject.settings.deploy && python manage.py migrate --settings=toyproject.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=toyproject.settings.deploy toyproject.wsgi --bind 0.0.0.0:8000"]