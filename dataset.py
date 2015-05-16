import json
import os, sys
import requests

from enum import Enum
"""
Uses the api from https://www.padherder.com/api/#data
"""

#hotfix openssl
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()

BASE_API = "https://www.padherder.com/api"
DATA_PATH = "data"


ApiTypes = Enum("ApiTypes", "ActiveSkills Awakenings Events Evolutions Food LeaderSkills Materials Monsters")
ApiTypeMap = {
    ApiTypes.ActiveSkills : "active_skills",
    ApiTypes.Awakenings : "awakenings",
    ApiTypes.Events : "events",
    ApiTypes.Evolutions : "evolutions",
    ApiTypes.Food : "food",
    ApiTypes.LeaderSkills : "leader_skills",
    ApiTypes.Materials : "materials",
    ApiTypes.Monsters : "monsters",
}

def assert_valid_api_path(path):
    """
    makes a HEAD request to the path, makes sure it 200s
    """
    resp = requests.head(path)
    try:
        resp.raise_for_status()
    except requests.exceptions.HTTPError:
        print 'ERROR', path, 'was not valid'
        raise

def build_api_path(api_type):
    return "{base}/{path}/".format(
        base=BASE_API,
        path=ApiTypeMap[api_type]
    )

def create_data_path():
    if not os.path.isdir(DATA_PATH):
        print 'creating data path at', DATA_PATH
        os.mkdir(DATA_PATH)

def get_from_api(api_type):
    api_path = build_api_path(api_type)
    assert_valid_api_path(api_path)

    resp = requests.get(api_path)
    j = resp.json()

    return j

def get_from_cache(api_type, verbose=False):
    pathstr = "{base}/{path}.json".format(
        base=DATA_PATH,
        path=ApiTypeMap[api_type]
    )

    if not os.path.exists(pathstr): 
        create_data_path()
        if verbose: print 'fetching', api_type
        val = get_from_api(api_type)
        with open(pathstr, 'w') as f:
            json.dump(val, f)
    else:
        if verbose: print 'using cached', api_type
        with open(pathstr) as f:
            val = json.load(f)

    return val

def get_all_raw_data(verbose=False):
    return dict(
        active_skills = get_from_cache(ApiTypes.ActiveSkills, verbose=verbose),
        awakenings = get_from_cache(ApiTypes.Awakenings, verbose=verbose),
        events = get_from_cache(ApiTypes.Events, verbose=verbose),
        evolutions = get_from_cache(ApiTypes.Evolutions, verbose=verbose),
        food = get_from_cache(ApiTypes.Food, verbose=verbose),
        leader_skills = get_from_cache(ApiTypes.LeaderSkills, verbose=verbose),
        materials = get_from_cache(ApiTypes.Materials, verbose=verbose),
        monsters = get_from_cache(ApiTypes.Monsters, verbose=verbose),
    )
