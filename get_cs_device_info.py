import inspect
import json
import sys

import requests

sys.path.append('/Users/alan/')
from secret import *
import logging

logging.basicConfig(level=logging.INFO, filename="app.log")


def get_cs_device_info() -> list:
    #
    # gets the name, ip_address of all of the console servers
    # initialises the port dictionary for each device
    #
    endpoint = NB_URL + 'devices/?limit=0&q=-cs-'

    logging.debug(f'{inspect.currentframe().f_code.co_name}: {endpoint}')

    response = requests.get(endpoint, headers=NB_HEADERS)
    json_dev_data = json.loads(response.content)

    cs_info = {}

    for cs in json_dev_data['results']:
        info = \
            {
                'name': cs['name'],
                'ipv4_address': cs['primary_ip4']['address'][:-3],
                'ports': {}
            }

        csid = cs['id']
        cs_info[csid] = info

    return cs_info


if __name__ == '__main__':
    results = get_cs_device_info()
    print(json.dumps(results, indent=2))
