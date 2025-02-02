FROM ubuntu:20.04
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    ffmpeg \
    libopus-dev \
    git \
    && apt-get clean
WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
CMD python3 -m userbot