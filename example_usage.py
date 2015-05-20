import sys
import argh

from pprint import pprint as pp

from pad import Pad
from filters import MonsterFilter
from constants import AttributeTypes

@argh.arg("monster_id", type=int, help="ID of the monster")
def get_monster(monster_id, verbose=False):
    """ outputs a monster's complete stats """
    padpy = Pad(verbose=verbose)

    monster = padpy.get_monster(monster_id)
    padpy.pretty_print(monster)

def get_all_monsters(verbose=False):
    """ outputs all monsters' complete stats """
    padpy = Pad(verbose=verbose)

    monsters = padpy.get_all_monsters()
    for monster in monsters:
        padpy.pretty_print(monster)
        print

@argh.arg("monster_id", type=int, help="ID of the monster")
@argh.arg("level", type=int, help="Target Level")
def calc_xp(monster_id, level, verbose=False):
    """ calculates XP required from level 1 to level """
    padpy = Pad(verbose=verbose)

    monster = padpy.get_monster(monster_id)
    calc_level = min(level, monster.max_level)
    if calc_level != level:
        print "{monster} is level capped at {max}!".format(
                monster=monster,
                max=monster.max_level,
        )

    print "From level 1 to level %s" % calc_level
    print "%s XP is required" % monster.xp_curve.calc_for_level(level)

@argh.arg("monster_id", type=int, help="ID of the monster")
@argh.arg("level", type=int, help="Target Level")
@argh.arg("attribute", type=str, choices=AttributeTypes._member_names_, help="Target Level")
@argh.arg("--plus", type=int, default=0, help="Plus stat")
def calc_attribute(monster_id, level, attribute, plus=0, verbose=False):
    """ 
    calculates the value for a given attribute at a given level (with plus values) 
    """
    padpy = Pad(verbose=verbose)

    monster = padpy.get_monster(monster_id)
    calc_level = min(level, monster.max_level)
    if calc_level != level:
        print "{monster} is level capped at {max}!".format(
                monster=monster,
                max=monster.max_level,
        )

    attr = AttributeTypes[attribute]
    attr_obj = monster.get_attribute(attr)

    result = attr_obj.calc_for_level_plus(calc_level, plus)
    print "Attribute %s at level %s plus %s" % (attr_obj, calc_level, plus)
    print "%s is the stat" % (result)

def get_events(verbose=False):
    """ 
    Gets all the events returned by the PADherder API. 
    Generally a few days worth.

    Note that these are cached, you'll need to delete data/events.json manually 
    if you want an updated list of events.
    """
    padpy = Pad(verbose=verbose)

    for evt in padpy.get_all_events():
        print evt

@argh.arg("user_id", type=int, help="User ID of the profile")
def get_user_profile(user_id, verbose=False):
    padpy = Pad(verbose=verbose)
    pp(padpy.get_user_profile(user_id))

@argh.arg("user_name", type=str, help="Username of the profile")
def get_user_data(user_name, verbose=False):
    padpy = Pad(use_monster_api=False, verbose=verbose)
    pp(padpy.get_user_data(user_name))


parser = argh.ArghParser()
parser.add_commands([
    get_monster,
    get_all_monsters,
    calc_xp,
    calc_attribute,
    get_events,
    get_user_profile,
    get_user_data,
])

if __name__ == "__main__":
    parser.dispatch()
