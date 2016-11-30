# Set the base image
FROM python:2.7

# File Author / Maintainer
MAINTAINER Des

# Update the sources list
RUN apt-get update


# Copy the application folder inside the container
ADD /SMFA /SMFA

# Get pip to download and install requirements:
RUN pip install -r /SMFA/requirements.txt

# Expose listener port
EXPOSE 8080

# Set the default directory where CMD will execute
WORKDIR /SMFA
# Set the default command to execute
# when creating a new container
CMD python app.py
