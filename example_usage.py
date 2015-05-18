import sys
import argh

from pad import Pad
from filters import MonsterFilter

@argh.arg("monster_id", type=int, help="ID of the monster")
def get_monster(monster_id, verbose=False):
    padpy = Pad(verbose=verbose)

    monster = padpy.get_monster(monster_id)
    padpy.pretty_print(monster)

def get_all_monsters(verbose=False):
    padpy = Pad(verbose=verbose)

    monsters = padpy.get_all_monsters()
    for monster in monsters:
        padpy.pretty_print(monster)
        print

parser = argh.ArghParser()
parser.add_commands([get_monster, get_all_monsters])

if __name__ == "__main__":
    parser.dispatch()
