FROM python:3.7
# Set image metadata
LABEL version="1.0"
LABEL description="Blog-api"
ENV PYTHONUNBUFFERED 1
# Create app directory
RUN mkdir /src
WORKDIR /src
ADD . /src/
# COPY requirements.txt /code/
RUN pip install -r requirements.txt
EXPOSE 8000