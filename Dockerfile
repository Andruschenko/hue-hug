FROM frolvlad/alpine-python3
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["hug", "-f", "src/hug.py"]