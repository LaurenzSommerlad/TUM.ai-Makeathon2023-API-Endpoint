FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code/

RUN rm -rf /code/pdfs
RUN mkdir /code/pdfs

EXPOSE 1234
CMD uvicorn app:app --host 0.0.0.0 --port 80