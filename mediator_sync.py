#!/usr/bin/env python3

"""
VMO3 - MEDIATOR SYNC
Author: Clint Mann

Description:
This is the Mediator Sync, it will
 make a REST API call and POST a 'hello' message
 with the Mediator to synchronize
"""

import requests
import datetime


def sync_mediator(sync_url):
    print('In Mediator Sync...')
    start = datetime.datetime.now()
    print('START sync', start)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(sync_url, headers=headers, timeout=35)

    end = datetime.datetime.now()
    print('END sync', end)

    resp = response.json()

    return resp
