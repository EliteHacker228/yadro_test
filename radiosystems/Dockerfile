FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y wget && \
    apt-get install -y python3 && \
    apt-get install -y python3-pip && \
    apt-get clean
COPY search_path.sh /tmp/search_path.sh
COPY extract_path_value.py /tmp/extract_path_value.py
COPY config.txt /tmp/config.txt
RUN chmod +x /tmp/search_path.sh
RUN chmod +x /tmp/extract_path_value.py