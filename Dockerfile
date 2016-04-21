FROM daocloud.io/python:2.7
MAINTAINER au9ustine
WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy our code from the current folder to /app inside the container
ADD . /app

# Make port 5000 available for links and/or publish
# EXPOSE 80

# Environment Variables
# ENV NAME World

# Define our command to be run when launching the container
