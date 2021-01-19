FROM python:3.8

RUN pip install git+https://github.com/gieeedreee/calculator.git

CMD [ "python" ]
