FROM ubuntu:14.04

# To mute debconf messages (see https://github.com/phusion/baseimage-docker/issues/58)
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

# Update and install some command-line tools + python plus required packages
# TODO: Remove unnecessary tools
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    curl \
    git \
    libfreetype6 \
    libopencv-dev \
    pkg-config \
    python2.7 \
    python2.7-dev \
    python-distribute \
    python-matplotlib \
    python-numpy \
    python-opencv \
    python-pip \
    tar \
    vim \
    wget \
&& pip install Flask


## If server was build once already, just comment all above this line and uncomment the line below
# FROM huehug_clairecut-server

COPY . /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]