import json
import os, sys
import requests

from functools import partial

from enum import Enum
"""
Uses the api from https://www.padherder.com/api/#data
"""

try:
    #hotfix openssl
    import urllib3.contrib.pyopenssl
    urllib3.contrib.pyopenssl.inject_into_urllib3()
except ImportError as e:
    print 'caught an error while trying to fix the warning in requests:', e, 'but continuing anyway'
    print 'check out https://stackoverflow.com/questions/18578439/using-requests-with-tls-doesnt-give-sni-support/18579484#18579484'

BASE_API = "https://www.padherder.com/api"
BASE_USER_API = "https://www.padherder.com/user-api"
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

UserApiTypes = Enum("ApiTypes", "User Profile Food Materials Monsters Teams")
UserApiTypeMap = {
    UserApiTypes.User : "user/{}",
    UserApiTypes.Profile : "profile/{}",
    UserApiTypes.Food : "food/{}",
    UserApiTypes.Materials : "material/{}",
    UserApiTypes.Monsters : "monster/{}",
    UserApiTypes.Teams : "team/{}",
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

def build_api_path(api_type, arg=None):
    if api_type in ApiTypes:
        base_path = BASE_API
        ext_path = ApiTypeMap[api_type]
    elif api_type in UserApiTypes:
        base_path = BASE_USER_API
        ext_path = UserApiTypeMap[api_type]
    else:
        print "Unrecognized ApiType"

    return "{base}/{path}/".format(
        base=base_path,
        path=ext_path.format(arg) if arg else ext_path,
    )

def create_data_path():
    if not os.path.isdir(DATA_PATH):
        print 'creating data path at', DATA_PATH,
        try:
            os.mkdir(DATA_PATH)
        except OSError as e:
            print "...couldn't create data directory. Run with admin permissions, or create the data directory manually"
            return False
        else:
            print
            return True

def get_from_api(api_type, arg=None, verbose=False):
    api_path = build_api_path(api_type, arg)
    assert_valid_api_path(api_path)

    resp = requests.get(api_path)
    j = resp.json()

    return j

def get_from_cache(api_type, verbose=False):
    pathstr = "{base}/{path}.json".format(
        base=DATA_PATH,
        path=ApiTypeMap[api_type] if api_type in ApiTypeMap else UserApiTypeMap[api_type]
    )

    if not os.path.exists(pathstr): 
        created = create_data_path()
        if verbose:
            if not created:
                print "Warning", api_type.name, "is not cached for next time"
            print 'fetching', api_type

        val = get_from_api(api_type, arg=arg)
        with open(pathstr, 'w') as f:
            json.dump(val, f)
    else:
        if verbose: print 'using cached', api_type.name
        with open(pathstr) as f:
            val = json.load(f)

    return val

def get_all_raw_data(verbose=False):
    get = partial(get_from_cache, verbose=verbose)
    return dict(
        active_skills = get(ApiTypes.ActiveSkills),
        awakenings = get(ApiTypes.Awakenings),
        events = get(ApiTypes.Events),
        evolutions = get(ApiTypes.Evolutions),
        food = get(ApiTypes.Food),
        leader_skills = get(ApiTypes.LeaderSkills),
        materials = get(ApiTypes.Materials),
        monsters = get(ApiTypes.Monsters),
    )

def get_raw_user_profile_data(user_id, verbose=False):
    get = partial(get_from_api, verbose=verbose)
    return dict(
            profile = get(UserApiTypes.Profile, arg=user_id),
    )

def get_raw_user_data(username, verbose=False):
    get = partial(get_from_api, verbose=verbose)
    return dict(
            get(UserApiTypes.User, arg=username),
    )
