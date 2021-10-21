#installing python
FROM python:3

USER root
RUN apt-get update && apt-get install python3-distutils -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

# create ictc repo
RUN mkdir ictc
WORKDIR /ictc/
COPY . .

RUN pip install -r requirements.txt
RUN pip install jupyter

CMD [ "python", "scraper_test.py" ]
