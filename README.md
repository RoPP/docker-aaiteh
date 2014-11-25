docker-aaiteh
=============

Tiny python script to add ip and hostname of container in /etc/hosts.

Installation
------------

```shell
sudo cp docker-aaiteh.py /usr/local/bin
sudo cp docker-aaiteh.service /etc/systemd/system
sudo systemctl enable docker-aaiteh.service
sudo systemctl start docker-aaiteh.service
```

Enjoy :)
