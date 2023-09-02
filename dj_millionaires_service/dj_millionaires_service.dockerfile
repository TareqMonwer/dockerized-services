FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

RUN chmod +x /code/prestart.sh
ENV PYTHONPATH=/code
# CMD ["./prestart.sh"]