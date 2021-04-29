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

        short_hostname = strip_device_name(hostname, 2)

        common = \
            f"Host {hostname} {short_hostname}\n" \
            f"  User                    alanc\n" \
            f"  Hostname                {cs_ip_address}\n" \
            f"  ProxyJump               alanc@nso-01\n\n"

        for port in cs_info[cs]['ports']:
            if cs_info[cs]['ports'][port]:
                hostname = shorten_console_name(cs_info[cs]['ports'][port])

                port_entry = \
                    f"Host {hostname} {strip_device_name(hostname, 2)}\n" \
                    f"  User                    alanc\n" \
                    f"  Hostname                {cs_ip_address}\n" \
                    f"  Port                    {port}\n" \
                    f"  ProxyJump               alanc@nso-01\n\n"

                common += port_entry

        print(common, end='')


if __name__ == '__main__':
    get_cs_info()

# logging.debug(stuff)
