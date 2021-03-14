FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

COPY . ./jpsite

CMD python manage.py makemigrations ; python manage.py migrate ; python manage.py collectstatic --noinput