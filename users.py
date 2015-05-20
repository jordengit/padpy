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

        self.id = kwargs['id']
        self.monster = self.pad.get_monster(kwargs['monster'])
        self.note = kwargs['note']
        self.priority = kwargs['priority']

        self.current_xp = kwargs['current_xp']
        self.current_skill = kwargs['current_skill']
        self.current_awakening = kwargs['current_awakening']

        self.plus_atk = kwargs['plus_atk']
        self.plus_hp = kwargs['plus_hp']
        self.plus_rcv = kwargs['plus_rcv']

        self.target_evolution = kwargs['target_evolution']
        self.target_level = kwargs['target_level']

        self.url = kwargs['url']

    def __str__(self):
        return "{monster} XP:{level}".format(
            monster=self.monster,
            level=self.current_xp,
        )

    def __repr__(self):
        return "<uMonster: %s>" % str(self)
