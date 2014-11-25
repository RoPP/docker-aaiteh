docker-aaiteh
=============

Tiny python script to add ip and hostname of container in /etc/hosts.

Installation
------------

Install [docker-py](https://github.com/docker/docker-py)

For debian :
```shell
sudo apt install python-docker
```

```shell
wget https://github.com/RoPP/docker-aaiteh/archive/master.zip
unzip master.zip
cd docker-aaiteh-master
sudo cp docker-aaiteh.py /usr/local/bin
sudo cp docker-aaiteh.service /etc/systemd/system
sudo systemctl enable docker-aaiteh.service
sudo systemctl start docker-aaiteh.service
```

Usage
-----

Nothing to do. When you start a container, it should be added to your /etc/hosts file with his ip address. It should be removed when you stop it.

Enjoy :)
