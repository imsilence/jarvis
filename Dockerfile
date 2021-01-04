FROM python:3.8.7

LABEL user="imsilence@outlook.com"

WORKDIR /opt/jarvis/

EXPOSE 8000/tcp

COPY . /opt/jarvis/

RUN apt-get -q update && \
    apt-get -qy install netcat && \
    /usr/local/bin/pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple -r /opt/jarvis/requirements.txt

ENTRYPOINT [ "/bin/bash", "/opt/jarvis/docker-entrypoint.sh" ]