#!/bin/bash
cd ~/lab/infrastructure/utility/containers/homepage
podman-compose down -t 2

cd ~/lab/infrastructure/utility/containers/phpipam
podman-compose down -t 2

cd ~/lab/infrastructure/utility/containers/portainer
podman-compose down -t 2

cd ~/lab/infrastructure/utility/containers/uptime-kuma
podman-compose down -t 2
