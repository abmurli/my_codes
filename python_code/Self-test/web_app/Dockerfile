FROM python:3.8.5-slim-buster
RUN mkdir /webapp
COPY ./requirements.txt /webapp/requirement.txt
RUN python3 -m pip install -r /webapp/requirement.txt
COPY . /webapp
EXPOSE 8080
WORKDIR /webapp
ENTRYPOINT ["python"]
CMD ["app.py"]
