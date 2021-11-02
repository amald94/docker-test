#installing python
FROM python:3

# USER root
# RUN apt-get update && apt-get install python3-distutils -y
# RUN wget https://bootstrap.pypa.io/get-pip.py
# RUN python3 get-pip.py

# create ictc repoRUN mkdir ictc
WORKDIR /ictc/
COPY . .

RUN pip install -r requirements.txt
RUN pip install jupyter
RUN pip install google-cloud-storage

CMD [ "python", "scraper_test.py" ]
