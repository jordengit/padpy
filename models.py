
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

        self.active_skill = kwargs['active_skill']
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

    def load_materials(self, materials):
        self.materials = []
        for m_id, count in materials:
            material = EvolutionCompontent(m_id, count, self)
            self.materials.append(material)

class EvolutionManager(object):
    def __init__(self, evolutions):
        self.load_evolutions(evolutions)

    def load_evolutions(self, evolutions):
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


