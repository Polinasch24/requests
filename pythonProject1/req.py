import json
from pprint import pprint


import requests

#
def get_h_int():
    url = "https://superheroapi.com/api/2619421814940190/search/Hulk/get"
    params = {"intelligence": 81}
    # headers = {"name": 'Hulk'}
    responce = requests.get(url=url)
    pprint (responce.json())
get_h_int()

def get_ca_int():
    url = "https://superheroapi.com/api/2619421814940190/search/Captain America/get"
    params = {'intelligence': 69}
    responce = requests.get(url=url, params=params)
    pprint (responce.json())
get_ca_int()

def get_t_int():
    url = "https://superheroapi.com/api/2619421814940190/search/Thanos/get"
    params = {'intelligence': 100}
    responce = requests.get(url=url, params=params)
    pprint (responce.json())
get_t_int()








