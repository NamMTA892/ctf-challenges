FROM python:latest

WORKDIR /app
COPY app.py ./
COPY requirements.txt ./
COPY templates templates
RUN chmod -R 775 .

RUN pip install -r requirements.txt

RUN useradd bksec
USER bksec

CMD python app.py
