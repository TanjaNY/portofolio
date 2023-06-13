FROM python:3.10.2-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . /code/
