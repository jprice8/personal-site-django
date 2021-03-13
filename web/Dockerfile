FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 

COPY . .