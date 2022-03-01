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

# expose port 5000
EXPOSE 5000

# run following command
CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]
