import json
import sys

import requests

sys.path.append('/Users/alan/')
from secret import *
import logging


# logging.basicConfig(level=logging.INFO, filename="app.log")


def get_cs_port_info(cs_info: list) -> list:
    device = ''
    endpoint = NB_URL + 'console-server-ports/?limit=0'  # ?q=&device_id=' + info['id']

    response2 = requests.get(endpoint, headers=NB_HEADERS)
    json_cs_data = json.loads(response2.content)

    for console in json_cs_data['results']:

        if device != console['device']['id']:
            device = console['device']['id']
            port_number = 4001

        try:
            cs_info[console['device']['id']]['ports'][port_number] = \
                console['connected_endpoint']['device']['name'] + \
                '-' + console['connected_endpoint']['name']

        except TypeError:
            cs_info[console['device']['id']]['ports'][port_number] = False
            pass

        port_number += 1

    return cs_info


if __name__ == '__main__':
    from get_cs_device_info import get_cs_device_info

    results = get_cs_device_info()
    get_cs_port_info(results)

# logging.debug(stuff)
