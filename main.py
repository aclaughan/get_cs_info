import inspect
import json
import sys

import requests as requests

sys.path.append('/Users/alan/')
from secret import *
import logging

logging.basicConfig(level=logging.INFO, filename="app.log")


def get_cs_info():
    #endpoint = NB_URL + 'console-server-ports/?q=&device_id=2584'
    endpoint = NB_URL + 'devices/?limit=0&q=-cs-'

    HEADERS = \
        {
            'Authorization': 'Token ' + NB_TOKEN,
            'Content - Type': 'application / json;charset = utf - 8'
        }

    logging.debug(f'{inspect.currentframe().f_code.co_name}: {endpoint}')

    response = requests.get(endpoint, headers=HEADERS)
    json_dev_data = json.loads(response.content)

    cs_info = []

    for cs in json_dev_data['results']:
        info = {}
        info['name'] = cs['name']
        info['ipv4_address'] = cs['primary_ip4']['address'][:-3]
        info['id'] = cs['id']
        endpoint = NB_URL + 'console-server-ports/?limit=0' #?q=&device_id=' + info['id']

        response2 = requests.get(endpoint, headers=HEADERS)
        json_cs_data = json.loads(response2.content)

        cs_info.append(info)

        endpoint = NB_URL + 'console-server-ports/?q=&device_id=' + info['id']

    print(f"{cs['name']:>18} {cs['primary_ip4']['address'][:-3]}")


if __name__ == '__main__':
    get_cs_info()

# logging.debug(stuff)
