FROM frolvlad/alpine-python3
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
VOLUME ./src /app/src
CMD ["hug", "-f", "src/hug.py"]