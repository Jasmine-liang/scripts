"""
Make BitQuery API calls concurrently.
"""

from datetime import date
import os
import json
import asyncio
from typing import Any
import aiohttp
import requests
from aws_lambda_powertools import Tracer
from aws_lambda_powertools.tracing import aiohttp_trace_config


tracer = Tracer()

bq_api_url = 'https://graphql.bitquery.io'
bq_api_key = 'BQY56IIMaKt42dVYCEjHstUGl5NMi0rx'


def handler(): 
    # (err_msg, token_addr, user_addr) = parse_function_input(event)
    
    headers = {
        'X-API-KEY': bq_api_key,
        'Access-Control-Request-Headers': '*',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': "DELETE, POST, GET, OPTIONS",
        'Access-Control-Allow-Headers': "Origin, Content-Type, Authorization, X-Requested-With",
    }

    token_addr = '0xbb0e17ef65f82ab018d8edd776e8dd940327b28b'
    query ="""
        {
            ethereum(network: ethereum) 
            {
                smartContractEvents(
                    smartContractAddress: {is: "%s"}
            ) {
                    count(uniq: callers)
                    date {
                        date
                        }
               }
            }
        }
        """ % (token_addr)
    

 
    res = requests.post(bq_api_url, headers=headers, json={'query': query})
    return (res.json())



res = (handler())
date_objs = res['data']['ethereum']['smartContractEvents']
cnt = 0
bp = 0
for i in range(len(date_objs)):
    if(date_objs[i]['date']['date'] == '2022-02-22'):
        bp = i
        break
# print(bp) 
for i in range(bp, len(date_objs)):
    cnt += date_objs[i]['count']  
print(cnt/30)