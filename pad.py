import sys
import json
import requests

from pprint import pprint as pp

from models import Pad
from filters import MonsterFilter
from dataset import get_all_raw_data
from constants import ElementTypes, TypeTypes

if __name__ == "__main__":
    pad = Pad(verbose=False)

    monster_id = int(sys.argv[1])
    m1 = pad.get_monster(monster_id)

    monsters = pad.get_all_monsters()

    monster_filter = MonsterFilter(monsters)


    by_type2 = monster_filter.by_type2(TypeTypes.Dragon)
    by_element2 = monster_filter.by_element2(ElementTypes.Fire)

    for monster in by_type2:
        print 'Monster #%s is: %s' % (monster.id, monster)
        ls = monster.leader_skill
        print "\tLeader Skill", ls
        ld = ls.data
        print "\tLeader Data", ld
        lc = ld.constraints
        print "\tLeader Constraints", lc
