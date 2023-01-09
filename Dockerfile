FROM arm64v8/ubuntu:22.04

RUN apt-get update \
 && export DEBIAN_FRONTEND=noninteractive \
 && apt-get -y install --no-install-recommends python-is-python3 python3-pip tzdata \
 && apt-get clean autoclean \
 && apt-get autoremove --yes \
 && rm -rf /var/lib{apt,dpkg,cache,log}/

COPY requirements.txt /tmp/pip-tmp/

RUN pip install --upgrade pip \
 && pip install --upgrade --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
 && rm -rf /tmp/pip-tmp

