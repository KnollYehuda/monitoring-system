FROM python:3.10-slim AS monitoring-system-builder

ARG docker_host='unix:///var/run/docker.sock'

# setup environment variable
ENV DOCKER_HOST=$docker_host
ENV WORKDIR=/src
ENV PYTHONPATH=/

# make docker accessible in container
RUN apt-get update \
 && apt-get install --no-install-recommends -y make curl apt-transport-https ca-certificates gnupg2 software-properties-common libpq-dev python-dev-is-python3 gcc\
 && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o/usr/share/keyrings/docker-archive-keyring.gpg \
 && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list \
 && apt update && apt install --no-install-recommends docker-ce-cli docker-compose-plugin -y \
 && apt purge -y apt-transport-https ca-certificates gnupg2 software-properties-common \
 && apt autoremove -y \
 && apt clean \
 && rm -rf /var/lib/apt/lists/*

# copy & install the python requirements
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /src
CMD ["/bin/bash"]

FROM monitoring-system-builder AS monitoring-system

COPY monitoring_system /monitoring_system

WORKDIR /
ENTRYPOINT monitoring_system/entrypoint.sh
