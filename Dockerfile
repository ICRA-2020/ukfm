FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
 && apt-get install -y \
    python3-pip \
    python3-tk \
 && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip

RUN mkdir /ukfm

COPY . /ukfm/.

RUN cd /ukfm/python \
 && python3 -m pip install -r requirements.txt

RUN cd /ukfm/python \
 && python3 -m pip install .

CMD ["python3", "/ukfm/python/demo.py"]
