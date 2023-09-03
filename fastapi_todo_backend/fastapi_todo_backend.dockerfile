FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
RUN chmod +x /code/app/prestart.sh
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
