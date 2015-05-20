import sys
import json
import requests

from dataset import get_all_raw_data, get_raw_user_data, UserApiTypes
from constants import ElementTypes, TypeTypes

from users import UserTeamManager, UserMonsterManager
from models import MonsterManager, EvolutionManager, ActiveSkillManager, \
        AwakeningManager, LeaderSkillManager, FoodManager, EventManager

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

    def __init__(self, use_monster_api=True, verbose=False):
        if use_monster_api:
            data = get_all_raw_data(verbose=verbose)
            self.monsters = MonsterManager(data['monsters'])
            self.evolutions = EvolutionManager(data['evolutions'])
            self.active_skills = ActiveSkillManager(data['active_skills'])
            self.awakenings = AwakeningManager(data['awakenings'])
            self.leader_skills = LeaderSkillManager(data['leader_skills'])
            self.food = FoodManager(data['food'])

            self.events = EventManager(data['events'])

    def get_user_profile(self, username, verbose=False):
        return get_raw_user_data(username, UserApiTypes.Profile, verbose=verbose)

    def get_user_data(self, username, verbose=False):
        return get_raw_user_data(username, verbose=verbose)

    def get_user_teams(self, username, verbose=False):
        team_data = get_raw_user_data(username, UserApiTypes.Teams, verbose=verbose)
        return UserTeamManager(team_data).objects

    def get_user_monsters(self, username, verbose=False):
        monster_data = get_raw_user_data(username, UserApiTypes.Monsters, verbose=verbose)
        return UserMonsterManager(monster_data).objects

    def populate_monster(self, monster):
        """ replaces placeholder data with real data """
        monster.active_skill = self.active_skills.get_by_id(monster.active_skill_name)
        monster.evolutions = self.evolutions.get_by_id(monster.id)
        monster.awoken_skills = self.awakenings.get_for_monster(monster)
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

    def get_all_events(self):
        return self.events.objects

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

    def pretty_print(self, monster):
        """ 
        outpus a complete monster information
        """

        print "  ", str(monster)
        print "Elements", monster.element, "/",  monster.element2
        print "Types", monster.type, "/",  monster.type2
        print
        print "Active Skill:", monster.active_skill
        print "Leader Skill:", monster.leader_skill
        print "Awoken Skills:", monster.awoken_skills
        print
        print "HP", monster.hp
        print "ATK", monster.atk
        print "RCV", monster.rcv
        print 
        print "Max level:", monster.max_level
        print "Team Cost:", monster.team_cost
        print "Feed XP:", monster.feed_xp
        print "XP Curve:", monster.xp_curve
        print
        print "Japan Only" if monster.jp_only else "Available Everywhere"
