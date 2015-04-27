docker-aaiteh
=============

Tiny python script to add ip and hostname of container in /etc/hosts.

Installation
------------

Install [docker-py](https://github.com/docker/docker-py)

For debian :
```shell
sudo apt install cmake python-docker
```

```shell
wget https://github.com/RoPP/docker-aaiteh/archive/master.zip
unzip master.zip
cd docker-aaiteh-master
mkdir build
cd build
cmake ..
sudo make install
sudo systemctl enable docker-aaiteh.service
sudo systemctl start docker-aaiteh.service
```

Usage
-----

Nothing to do. When you start a container, it should be added to your /etc/hosts file with his ip address. It should be removed when you stop it.

Enjoy :)
