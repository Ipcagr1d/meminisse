# use python image version 3.8
FROM python:3.8

# set workdir
WORKDIR /usr/src/app

# copy requirements only then install the requirements
COPY requirements.txt requirements.txt

# install requirements
RUN pip3 install -r requirements.txt

# copy all file to folder
COPY . .

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["wsgi.py" ]