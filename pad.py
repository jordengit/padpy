import sys
import json
import requests

from dataset import get_all_raw_data
from constants import ElementTypes, TypeTypes
from models import MonsterManager, EvolutionManager, ActiveSkillManager, \
        AwakeningManager, LeaderSkillManager, FoodManager

class Pad(object):
    """
    This is the main object you'll be using to access all the data

    >>> pad = Pad(verbose=False)
    >>> monsters = pad.get_all_monsters()
    >>> ice_ogre = pad.get_monster(65)
    >>> ice_ogre.feed_xp
    <FeedExp 413.0>
    >>> ice_ogre.feed_xp.calc_for_level(12)
    4956.0
    >>> ice_ogre.atk
    <Attribute 277/875 * 1.0>

    >>> monsters_in_ice_ogre_tree = pad.get_evolution_tree(ice_ogre)
    [<Monster #64 Blue Ogre>,
     <Monster #65 Ice Ogre>,
     <Monster #312 Blazing Ice Ogre>,
     <Monster #313 Wood Ice Ogre>]
    """

    def __init__(self, verbose=False):
        data = get_all_raw_data(verbose=verbose)
        self.monsters = MonsterManager(data['monsters'])
        self.evolutions = EvolutionManager(data['evolutions'])
        self.active_skills = ActiveSkillManager(data['active_skills'])
        self.awakenings = AwakeningManager(data['awakenings'])
        self.leader_skills = LeaderSkillManager(data['leader_skills'])
        self.food = FoodManager(data['food'])


    def populate_monster(self, monster):
        """ replaces placeholder data with real data """
        monster.active_skill = self.active_skills.get_by_id(monster.active_skill_name)
        monster.evolutions = self.evolutions.get_by_id(monster.id)
        monster.awakenings = self.awakenings.get_for_monster(monster)
        monster.leader_skill = self.leader_skills.get_for_monster(monster)
        return monster

    def get_monster(self, id):
        monster = self.monsters.get_by_id(id)
        self.populate_monster(monster)
        return monster

    def get_all_raw_monsters(self):
        """ get all monster objects before they've been fully populated """
        return self.sort(self.monsters.objects)

    def get_all_monsters(self):
        return self.sort([self.populate_monster(m) for m in self.get_all_raw_monsters()])

    def sort(self, monsters):
        return sorted(monsters, key=lambda monster: monster.id)

    def get_evolution_tree(self, monster):
        """ 
        find all evolutions that either come from, or start before this monster
        """
        tree = [monster]
        #before
        prevos_to_check = self.evolutions.get_by_evolves_to(monster.id)
        while prevos_to_check:
            prevo_check = self.get_monster(prevos_to_check.pop().monster_id)
            if prevo_check not in tree:
                tree.append(prevo_check)
                for prevo in self.evolutions.get_by_evolves_to(prevo_check.id):
                    prevos_to_check.append(prevo)

        #after
        evos_to_check = monster.evolutions
        while evos_to_check:
            check_monster = self.get_monster(evos_to_check.pop().evolves_to)
            if check_monster not in tree:
                tree.append(check_monster)
                for evo in check_monster.evolutions:
                    evos_to_check.append(evo)

        return self.sort(tree)
