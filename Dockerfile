# Pull base image.
FROM ubuntu:18.04

# Set environment variables.
ENV HOME /root
ENV DISCORD_TOKEN <Token>
ENV DISCORD_CLIENT_ID <client_ID>

# Define working directory.
WORKDIR /root

# Add files.
ADD . /root

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y software-properties-common && \
  apt-get install -y firefox && \
  apt-get install -y python3-pip && \
  apt-get install -y wget && \
  python3 -m pip install --upgrade pip && \
  python3 -m pip install -r requirements.txt && \
  wget https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz && \
  tar -zxvf geckodriver-v0.27.0-linux64.tar.gz && \
  mv geckodriver /usr/bin && \
  rm -rf /var/lib/apt/lists/*

# Define default command.
CMD ["python3", "./cleverbot.py"]
