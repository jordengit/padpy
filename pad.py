import json
import requests

from dataset import get_all_raw_data
from models import EvolutionManager, EvolutionCompontent, MonsterManager

if __name__ == "__main__":
    data = get_all_raw_data()

    monsters = data['monsters']
    mon_manager = MonsterManager(monsters)
    evolutions = data['evolutions']
    evo_manager = EvolutionManager(evolutions)
    m1 = mon_manager.get_by_id(1)
    m1e = evo_manager.get_by_id(m1.id)


raw_input("Are you done here?\n> ")
