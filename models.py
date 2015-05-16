from dataset import get_all_raw_data

class Pad(object):
    def __init__(self):
        data = get_all_raw_data()
        self.monsters = MonsterManager(data['monsters'])
        self.evolutions = EvolutionManager(data['evolutions'])
        self.active_skills = ActiveSkillManager(data['active_skills'])
        self.awakenings = AwakeningManager(data['awakenings'])

    def get_monster(self, id):
        monster = self.monsters.get_by_id(id)
        monster.active_skill = self.active_skills.get_by_id(monster.active_skill_name)
        monster.evolutions = self.evolutions.get_by_id(monster.id)
        monster.awakenings = self.awakenings.get_for_monster(monster)

        return monster

class MonsterManager(object):
    def __init__(self, monsters):
        self.load_data(monsters)

    def load_data(self, monsters):
        self.monsters = []
        for monster in monsters:
            mon_obj = Monster(**monster)
            self.monsters.append(mon_obj)

    def get_by_id(self, id):
        monsters =  filter(lambda monster: int(monster.id) == int(id), self.monsters)
        if monsters:
            assert(len(monsters)==1)# there should only be 1 monster with this id
            return monsters[0] 
        else:
            return None

class ActiveSkillManager(object):
    def __init__(self, active_skills):
        self.load_data(active_skills)

    def load_data(self, active_skills):
        self.active_skills = []
        for skill in active_skills:
            try:
                mon_obj = ActiveSkill(
                    skill['min_cooldown'],
                    skill['effect'],
                    skill['max_cooldown'],
                    skill['name'],
                )
                self.active_skills.append(mon_obj)
            except Exception as e:
                print e
                print skill

    def get_by_id(self, name):
        active_skills =  filter(lambda skill: skill.name == name, self.active_skills)
        if active_skills:
            assert(len(active_skills)==1)# there should only be 1 activity with this id
            return active_skills[0] 
        else:
            return None

class ActiveSkill(object):
    def __init__(self, min_cooldown, effect, max_cooldown, name):
        self.min_cooldown = int(min_cooldown)
        self.effect = effect
        self.max_cooldown = int(max_cooldown)
        self.name = name

    def __str__(self):
        return "ActiveSkill: {name}".format(
                name=self.name
        )

    def __repr__(self):
        return str(self)



class Image(object):
    def __init__(self, href, size, owner):
        self.href = href
        self.size = size
        self.owner = owner

class Attribute(object):
    def __init__(self, max, min, scale, owner):
        self.max = max
        self.min = min
        self.scale = scale
        self.owner = owner

class Monster(object):
    def __init__(self, **kwargs):
        self.load_data(**kwargs)

    def __str__(self):
        return "#{id} {name}".format(
            id=self.id,
            name=self.name,
        )

    def __repr__(self):
        return "<Monster "+str(self)+">"

    def load_data(self, **kwargs):
        self.id = kwargs['id']
        self.version = kwargs['version']

        self.rarity = kwargs['rarity']
        self.max_level = kwargs['max_level']
        self.team_cost = kwargs['team_cost']
        self.feed_xp = kwargs['feed_xp']
        self.xp_curve = kwargs['xp_curve']

        self.active_skill = ActiveSkill(0, 'Unset Active Skill', 0, 'Unset Active Skill Name')
        self.active_skill_name = kwargs['active_skill']
        self.awoken_skills = kwargs['awoken_skills']
        self.leader_skill = kwargs['leader_skill']

        self.element = kwargs['element']
        self.element2 = kwargs['element2']
        self.type = kwargs['type']
        self.type2 = kwargs['type2']


        self.hp = Attribute(
            kwargs['hp_max'],
            kwargs['hp_min'],
            kwargs['hp_scale'],
            self,
        )
        self.atk = Attribute(
            kwargs['atk_max'],
            kwargs['atk_min'],
            kwargs['atk_scale'],
            self,
        )
        self.rcv = Attribute(
            kwargs['rcv_max'],
            kwargs['rcv_min'],
            kwargs['rcv_scale'],
            self,
        )

        self.name = kwargs['name']
        self.name_jp = kwargs['name_jp']

        self.image40 = Image(
            kwargs['image40_href'],
            kwargs['image40_size'],
            self,
        )

        self.image60 = Image(
            kwargs['image60_href'],
            kwargs['image60_size'],
            self,
        )

        self.jp_only = kwargs['jp_only']

class EvolutionCompontent(object):
    def __init__(self, monster_id, count, owner):
        self.monster_id = monster_id
        self.count = count

class Evolution(object):
    def __init__(self, monster_id, is_ultimate, evolves_to, materials):
        self.monster_id = int(monster_id)
        self.is_ultimate = is_ultimate
        self.evolves_to = int(evolves_to)

        self.load_materials(materials)

    def __str__(self):
        return "Evolution: {base} -> {into}".format(
            base=self.monster_id,
            into=self.evolves_to,
        )

    def __repr__(self):
        return "<{str}>".format(
            str=str(self)
        )

    def load_materials(self, materials):
        self.materials = []
        for m_id, count in materials:
            material = EvolutionCompontent(m_id, count, self)
            self.materials.append(material)

class EvolutionManager(object):
    def __init__(self, evolutions):
        self.load_data(evolutions)

    def load_data(self, evolutions):
        self.evolutions = []
        for monster_id, evo_set in evolutions.iteritems():
            for evo_data in evo_set:
                evo = Evolution(
                    monster_id,
                    evo_data['is_ultimate'],
                    evo_data['evolves_to'],
                    evo_data['materials'],
                )
                self.evolutions.append(evo)

    def get_by_id(self, id):
        return filter(lambda evo: int(evo.monster_id) == int(id), self.evolutions)


class Awakening(object):
    def __init__(self, id, name, description):
        self.id = int(id)
        self.name = name
        self.description = description

    def __str__(self):
        return "Awakening: #{id} {name}".format(
            id=self.id,
            name=self.name,
        )

    def __repr__(self):
        return "<{str}>".format(
            str=str(self)
        )

class AwakeningManager(object):
    def __init__(self, evolutions):
        self.load_data(evolutions)

    def load_data(self, awakenings):
        self.awakenings = []
        for data in awakenings:
            try:
                awake = Awakening(
                    data['id'],
                    data['name'],
                    data['desc'],
                )
                self.awakenings.append(awake)
            except Exception as e:
                print e
                print data

    def get_for_monster(self, monster):
        awakes = []
        for awk_id in monster.awoken_skills:
            awk = self.get_by_id(awk_id)
            awakes.append(awk)
        return awakes


    def get_by_id(self, id):
        result = filter(lambda awake: int(awake.id) == int(id), self.awakenings)
        if result:
            assert(len(result)==1)
            return result[0]
        return result

