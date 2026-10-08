

FROM ubuntu:latest
# Using / is a bad practice since it clutters main folder , so i'm using the future mounted folder to start the docker  
WORKDIR /python-rest-todo


#Skip python questions , this assumes the end user is not a OS front-end user 
ENV DEBIAN_FRONTEND=noninteractive

#Install basic python packages
RUN apt-get update && apt-get install -y\
    python3 \
    python3-pip \
    python3-venv

#REQUIRED VENV established by PEP 668
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m venv $VIRTUAL_ENV

#Install framework packages
RUN pip3 install \
    django \
    djangorestframework

#Start application
CMD ["python3",   "manage.py" ,  "runserver"]