import json
import requests

from dataset import get_all_raw_data
from models import Pad

if __name__ == "__main__":
    pad = Pad()

    m1 = pad.monsters.get_by_id(1)
    m1e = pad.evolutions.get_by_id(m1.id)
    m1a = pad.active_skills.get_by_id(m1.active_skill)



raw_input("Are you done here?\n> ")
