import sys
import argh

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

parser = argh.ArghParser()
parser.add_commands([
    get_monster,
    get_all_monsters,
    calc_xp,
    calc_attribute,
])

if __name__ == "__main__":
    parser.dispatch()
