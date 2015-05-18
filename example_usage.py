import sys

from pad import Pad
from filters import MonsterFilter

if __name__ == "__main__":
    padpy = Pad(verbose=True)

    monster_id = int(sys.argv[1])
    m1 = padpy.get_monster(monster_id)

    monsters = padpy.get_all_monsters()
    for monster in monsters:
        padpy.pretty_print(monster)
