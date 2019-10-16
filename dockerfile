FROM python:3

MAINTAINER yash

COPY ./code.py .

ENTRYPOINT [ "python3", "code.py" ]
