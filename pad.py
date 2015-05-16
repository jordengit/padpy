import json
import requests

from pprint import pprint as pp

from dataset import get_all_raw_data
from models import Pad

if __name__ == "__main__":
    pad = Pad()

    m1 = pad.get_monster(65)
    m1e = pad.evolutions.get_by_id(m1.id)
    m1a = pad.active_skills.get_by_id(m1.active_skill)

    monsters = pad.get_all_monsters()
