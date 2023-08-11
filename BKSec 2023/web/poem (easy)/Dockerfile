FROM python:latest

WORKDIR /app
COPY app.py ./
COPY phlag.txt ./
COPY templates templates
COPY poems poems
COPY static static
RUN chmod -R 775 .

RUN pip install flask

RUN useradd bksec
USER bksec

CMD python app.py
