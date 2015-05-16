from dataset import get_all_data

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
        self.loaddata(**kwargs)

    def __str__(self):
        return "#{id} {name}".format(
            id=self.id,
            name=self.name,
        )

    def __repr__(self):
        return "<Monster "+str(self)+">"

    def loaddata(self, **kwargs):
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


