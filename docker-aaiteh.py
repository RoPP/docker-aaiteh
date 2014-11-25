#!/usr/bin/env python

import sys
import os
import shutil
import signal
import json
import docker


def read_etchosts():
    data = []
    with open('/etc/hosts') as hosts:
        for line in hosts:
            data.append(line)

    return data


def write_etchosts(data):
    with open('/etc/hosts', 'w') as hosts:
        hosts.writelines(data)


def update_hosts(status, name, ipaddress):
    hostname = name.strip('/') + '.docker'
    data = read_etchosts()
    new_data = []
    if status == 'die':
        for line in data:
            if hostname not in line:
                new_data.append(line)
    else:
        new_data = data
        new_data.append("%s\t%s\n" % (ipaddress, hostname))
    write_etchosts(new_data)


def bye(signal, frame):
    os.rename('/etc/hosts.origin', '/etc/hosts')
    sys.exit()


if __name__ == '__main__':

    signal.signal(signal.SIGINT, bye)
    signal.signal(signal.SIGTERM, bye)

    shutil.copyfile('/etc/hosts', '/etc/hosts.origin')

    client = docker.Client(base_url='unix://run/docker.sock')

    for str_event in client.events():
        event = json.loads(str_event)
        status = event.get('status')
        if status in ('start', 'die'):
            container = client.inspect_container(event.get('id'))
            network_settings = container.get('NetworkSettings')
            ipaddress = network_settings.get('IPAddress')
            name = container.get('Name')

            update_hosts(status, name, ipaddress)
