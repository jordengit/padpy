import json
import requests

from dataset import get_all_raw_data
from models import EvolutionManager, MonsterManager, ActiveSkillManager
from models import EvolutionCompontent

if __name__ == "__main__":
    data = get_all_raw_data()

    monsters = data['monsters']
    mon_manager = MonsterManager(monsters)
    evolutions = data['evolutions']
    evo_manager = EvolutionManager(evolutions)
    active_skills = data['active_skills']
    act_skill_manager = ActiveSkillManager(active_skills)

    m1 = mon_manager.get_by_id(1)
    m1e = evo_manager.get_by_id(m1.id)
    m1a = act_skill_manager.get_by_id(m1.active_skill)



raw_input("Are you done here?\n> ")
