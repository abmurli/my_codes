# our base image
FROM python:3.5.6-alpine3.8

# install Python modules needed by the Python app

RUN pip install flask

# copy files required for the app to run
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "/usr/src/app/app.py"]
