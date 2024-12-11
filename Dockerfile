FROM tiangolo/uvicorn-gunicorn:python3.8

RUN apt-get update
RUN apt-get install -y libsndfile1
RUN pip install --upgrade pip


WORKDIR /code/fast-auth
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5005"]

