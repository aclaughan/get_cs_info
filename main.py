import inspect
import json
import sys

import requests as requests

from get_cs_device_info import get_cs_device_info
from get_cs_port_info import get_cs_port_info
from shorten_console_name import shorten_console_name
from strip_device_name import strip_device_name

sys.path.append('/Users/alan/')
from secret import *
import logging

logging.basicConfig(level=logging.INFO, filename="app.log")


def get_cs_info():
    cs_info = get_cs_device_info()
    cs_info = get_cs_port_info(cs_info)

    for cs in cs_info.keys():
        hostname = cs_info[cs]['name']
        cs_ip_address = cs_info[cs]['ipv4_address']

        common = \
            f"Host {hostname} {strip_device_name(hostname, 2)}\n" \
            f"  User                    alanc\n" \
            f"  Hostname                {cs_ip_address}\n" \
            f"  ProxyJump               alanc@nso-01\n\n"

        port_number = 5001

        for port in cs_info[cs]['ports']:
            if port:
                port_number = port.keys[0]
                hostname = shorten_console_name(port[port_number])

                port_entry = \
                    f"Host {hostname} {strip_device_name(hostname, 2)}\n" \
                    f"  User                    alanc\n" \
                    f"  Hostname                {cs_ip_address}\n" \
                    f"  Port                    {port_number}" \
                    f"  ProxyJump               alanc@nso-01\n\n"

                common += port_entry
                port_number += 1

        print(common)


if __name__ == '__main__':
    get_cs_info()

# logging.debug(stuff)
