from models import BaseManager

class BaseUserManager(BaseManager):
    pass_pad = True

    def __init__(self, pad, data):
        self.pad = pad
        super(BaseUserManager, self).__init__(data)

class UserTeamManager(BaseUserManager):
    @property
    def model(self):
        return UserTeam

class UserTeam(object):
    def __init__(self, **kwargs):
        self.pad = kwargs['pad']

        self.id = kwargs['id']
        self.name = kwargs['name']
        self.favourite = kwargs['favourite']
        self.description = kwargs['description']

        self.leader = kwargs['leader']
        self.sub1 = kwargs['sub1']
        self.sub2 = kwargs['sub2']
        self.sub3 = kwargs['sub3']
        self.sub4 = kwargs['sub4']
        self.order = kwargs['order']

        self.friend_leader = kwargs['friend_leader']
        self.friend_level = kwargs['friend_level']
        self.friend_hp = kwargs['friend_hp']
        self.friend_atk = kwargs['friend_atk']
        self.friend_rcv = kwargs['friend_rcv']
        self.friend_skill = kwargs['friend_skill']
        self.friend_awakening = kwargs['friend_awakening']

    def __str__(self):
        return "{name}".format(
            name=self.name,
        )

    def __repr__(self):
        return "<uTeam: %s>" % str(self)

class UserMonsterManager(BaseUserManager):
    @property
    def model(self):
        return UserMonster

class UserMonster(object):
    def __init__(self, **kwargs):
        self.pad = kwargs['pad']
        self.load_data(**kwargs)

    def __str__(self):
        plus_val = self.plus_atk_raw+self.plus_hp_raw+self.plus_rcv_raw
        plus = "+{}".format(plus_val) if plus_val else ""

        return "{monster}{plus} Lv:{level}".format(
            monster=self.monster.name,
            plus=plus,
            level=self.current_level,
        )

    def __repr__(self):
        return "<uMonster: %s>" % str(self)

    def load_data(self, **kwargs):

        self.id = kwargs['id']
        self.monster = self.pad.get_monster(kwargs['monster'])
        self.note = kwargs['note']
        self.priority = kwargs['priority']

        self.current_xp = int(kwargs['current_xp'])
        self.current_level = self.monster.xp_curve.calc_for_xp(self.current_xp)
        self.current_skill = kwargs['current_skill']
        self.current_awakening = kwargs['current_awakening']

        self.plus_hp_raw = kwargs['plus_hp']
        self.plus_hp = self.monster.hp.calc_for_level_plus(
            self.current_level,
            self.plus_hp_raw
        )
        self.plus_atk_raw = kwargs['plus_atk']
        self.plus_atk = self.monster.atk.calc_for_level_plus(
            self.current_level,
            self.plus_atk_raw
        )
        self.plus_rcv_raw = kwargs['plus_rcv']
        self.plus_rcv = self.monster.rcv.calc_for_level_plus(
            self.current_level,
            self.plus_rcv_raw
        )

        self.target_evolution = kwargs['target_evolution']
        self.target_level = kwargs['target_level']

        self.url = kwargs['url']
