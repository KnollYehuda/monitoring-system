FROM python:3.10-slim AS monitoring-system-builder

ARG docker_host='unix:///var/run/docker.sock'

# setup environment variable
ENV DOCKER_HOST=$docker_host
ENV WORKDIR=/src
ENV PYTHONPATH=/

# make docker accessible in container
RUN apt-get update \
 && apt-get install --no-install-recommends -y make curl apt-transport-https ca-certificates gnupg2 software-properties-common \
 && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o/usr/share/keyrings/docker-archive-keyring.gpg \
 && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list \
 && apt update && apt install --no-install-recommends docker-ce-cli docker-compose-plugin -y \
 && apt purge -y apt-transport-https ca-certificates gnupg2 software-properties-common \
 && apt autoremove -y \
 && apt clean \
 && rm -rf /var/lib/apt/lists/*

# copy & install the python requirements
COPY requirements-builder.txt /requirements-builder.txt
RUN pip install -r requirements-builder.txt

# using docker from the builder container
RUN mkdir -m777 -p ${IBEX_OUTPUT} /.docker

WORKDIR /src
CMD ["/bin/bash"]

FROM python:3.10-slim AS monitoring-system

ARG docker_host='unix:///var/run/docker.sock'

# setup environment variable
ENV DOCKER_HOST=$docker_host
ENV PYTHONPATH=/

# make docker accessible in container
RUN apt-get update \
 && apt-get install --no-install-recommends -y make curl apt-transport-https ca-certificates gnupg2 software-properties-common \
 && curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o/usr/share/keyrings/docker-archive-keyring.gpg \
 && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list \
 && apt update && apt install --no-install-recommends docker-ce-cli docker-compose-plugin -y \
 && apt purge -y apt-transport-https ca-certificates gnupg2 software-properties-common \
 && apt autoremove -y \
 && apt clean \
 && rm -rf /var/lib/apt/lists/*

COPY monitoring_system /monitoring_system

# copy & install the python requirements
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# using docker from the builder container
RUN mkdir -m777 -p ${IBEX_OUTPUT} /.docker

WORKDIR /
ENTRYPOINT monitoring_system/entrypoint.sh
