#!/usr/bin/env python

import sys
import signal
import json
import docker

START_TAG = "### Add by docker-aaiteh. Do not edit.\n"
CONTAINERS = {}
INITIAL = []


def read_etchosts():
    with open('/etc/hosts') as hosts:
        for line in hosts:
            if line == START_TAG:
                return
            INITIAL.append(line)


def write_etchosts(data=[]):
    with open('/etc/hosts', 'w') as hosts:
        hosts.writelines(INITIAL)
        hosts.writelines(data)


def update_hosts(status, name, ipaddress):
    hostname = name.strip('/') + '.docker'
    if status == 'die':
        CONTAINERS.pop(hostname)
    else:
        CONTAINERS[hostname] = ipaddress

    data = [START_TAG]
    for h, i in CONTAINERS.items():
        data.append("%s\t%s\n" % (i, h))
    write_etchosts(data)


def process_container(container, status):
    network_settings = container.get('NetworkSettings')
    ipaddress = network_settings.get('IPAddress')
    name = container.get('Name')
    update_hosts(status, name, ipaddress)


def bye(signal, frame):
    write_etchosts()
    sys.exit()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, bye)
    signal.signal(signal.SIGTERM, bye)

    read_etchosts()
    client = docker.Client(base_url='unix://run/docker.sock')

    # Process running containers
    for c in client.containers():
        process_container(client.inspect_container(c['Id']), c['Status'])

    for str_event in client.events():
        event = json.loads(str_event)
        status = event.get('status')
        if status in ('start', 'die', 'create'):
            container = client.inspect_container(event.get('id'))
            process_container(container, status)
