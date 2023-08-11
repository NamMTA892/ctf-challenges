FROM python:latest

WORKDIR /challenge

COPY .server.py ./
COPY .xin_flag ./
COPY flag.txt ./
RUN chmod 751 .xin_flag
RUN chmod 755 .server.py

RUN pip install python-dotenv
RUN pip install colorama

RUN useradd bksec
USER bksec

CMD [ "python", "./.server.py" ]
