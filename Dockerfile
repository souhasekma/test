FROM python:3

WORKDIR /lasttest

COPY requirements.txt /requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /lasttest
