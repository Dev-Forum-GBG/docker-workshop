FROM python:3.10-slim

RUN mkdir app

WORKDIR /app

#COPY ./application/* ./
COPY ./application/requirements.txt ./

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]

