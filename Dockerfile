FROM ubuntu:16.04

#3.4.3
ENV PYTHON_VERSION 2.7

# Install OpenCV 3.0
RUN apt-get -y update

RUN apt-get -y install build-essential
RUN apt-get -y install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
RUN apt-get -y install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev \
                       libjasper-dev libdc1394-22-dev qtbase5-dev
RUN apt-get -y install unzip wget
#RUN apt-get -y install ffmpeg libopencv-dev libgtk-3-dev python-numpy python3-numpy \
#                       libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff5-dev \
#                       libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libxine2-dev \
#                       libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libv4l-dev libtbb-dev \
#                       qtbase5-dev libmp3lame-dev libopencore-amrnb-dev \
#                       libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils \
#                       unzip wget

RUN apt-get -y install python$PYTHON_VERSION-dev
RUN apt-get -y install python-pip python-tk

RUN wget https://github.com/opencv/opencv/archive/3.1.0.zip -O opencv3.zip && \
    unzip -q opencv3.zip && mv /opencv-3.1.0 /opencv
RUN mkdir /opencv/build
WORKDIR /opencv/build
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D WITH_CUBLAS=ON ..
RUN make
RUN make install
RUN /bin/bash -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
RUN ldconfig

RUN pip install numpy matplotlib Flask jsonify request image Pillow

## If server was build once already, just comment all above this line and uncomment the line below
# FROM huehug_clairecut-server

COPY . /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]
