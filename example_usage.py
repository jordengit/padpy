import sys
import argh

from pad import Pad
from filters import MonsterFilter

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

parser = argh.ArghParser()
parser.add_commands([
    get_monster,
    get_all_monsters,
    calc_xp,
])

if __name__ == "__main__":
    parser.dispatch()
