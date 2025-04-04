#!/bin/bash
cd ~/lab/infrastructure/utility/containers/homepage
podman-compose build
podman-compose up -d
sudo chown -R ubuntu:ubuntu volumes/config

cd ~/lab/infrastructure/utility/containers/phpipam
podman-compose build
podman-compose up -d

cd ~/lab/infrastructure/utility/containers/portainer
podman-compose build
podman-compose up -d

cd ~/lab/infrastructure/utility/containers/uptime-kuma
podman-compose build
podman-compose up -d
