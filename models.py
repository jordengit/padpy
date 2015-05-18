from constants import *
from dataset import get_all_raw_data

class BaseManager(object):
    """
    This manages a creates a list of objects from 
    a JSON list from the PADHerder API and instantiates
    full objects
    """

    identifier = "id" #used to identify its objects in get_by_id

    can_find_many = False #whether to return one or a list in get_by_id
    has_default_object = False #whether to return a default object in get_by_id

    nested_list = False #special load_data handling case
    nested_dict = False #special load_data handling case

    def __init__(self, data):
        self.load_data(data)

    @property
    def model(self):
        """ The Model this is managing """
        return None

    def build_obj(self, **kwargs):
        """ create the Model instance """
        return self.model(**kwargs)

    def load_data(self, data):
        """ go through the raw data and instantiate the objects """
        self.objects = []
        if not self.nested_list and not self.nested_dict:
            for d in data:
                obj = self.build_obj(**d)
                self.objects.append(obj)
        elif self.nested_list:
            for key, obj_set in data.iteritems():
                for obj_data in obj_set:
                    obj = self.model(
                        key,
                        **obj_data
                    )
                    self.objects.append(obj)
        elif self.nested_dict:
            for key, obj_set in data.iteritems():
                for obj_key, obj_data in obj_set.iteritems():
                    obj = self.model(
                        key,
                        obj_key,
                        obj_data
                    )
                    self.objects.append(obj)

    def get_by_id(self, id):
        """ 
        filter through the objects, returning either a 
        list or a single object, depending on can_find_many 
        and has_default_object
        """
        objects =  filter(lambda obj: getattr(obj, self.identifier) == id, self.objects)
        if not self.can_find_many:
            if objects:
                assert(len(objects)==1)# there should only be 1 object with this id
                return objects[0] 

        if not objects and self.has_default_object:
            return self.get_default_object()

        return objects

class MonsterManager(BaseManager):
    @property
    def model(self):
        return Monster

class ActiveSkillManager(BaseManager):
    identifier = "name"
    has_default_object = True

    @property
    def model(self):
        return ActiveSkill

    def build_obj(self, **skill):
        return  self.model(
            skill['min_cooldown'],
            skill['effect'],
            skill['max_cooldown'],
            skill['name'],
        )

    def get_default_object(self):
        return ActiveSkill("0", "No Effect", "0", "No Active Skill")

class ActiveSkill(object):
    def __init__(self, min_cooldown, effect, max_cooldown, name):
        self.min_cooldown = int(min_cooldown)
        self.effect = effect
        self.max_cooldown = int(max_cooldown)
        self.name = name

    def __str__(self):
        return "ActiveSkill: {name}".format(
            name=self.name.encode('utf8')
        )

    def __repr__(self):
        return "<%s>" % str(self)


class Image(object):
    def __init__(self, type, href, size, owner):
        self.type = type
        self.href = href
        self.size = size
        self.owner = owner

    def __str__(self):
        return "Image: {type} for #{id}".format(
            type=self.type,
            id=self.owner.id,
        )

    def __repr__(self):
        return "<%s>" % str(self)

class XpCurve(object):
    def __init__(self, id):
        self.id = id

    @property
    def long_name(self):
        return XpCurveIds[self.id].name

    def __str__(self):
        return "XP Curve {}".format(
            self.long_name,
        )

    def __repr__(self):
        return "<{}>".format(
            str(self)
        )

    def calc_for_level(self, level):
        return  round(self.id * (((level-1.0)/98.0)**2.5))

class FeedXp(object):
    def __init__(self, base_xp):
        self.base_xp = base_xp
        pass

    def __str__(self):
        return "FeedExp {}".format(
            self.base_xp,
        )

    def __repr__(self):
        return "<{}>".format(
            str(self)
        )

    def calc_for_level(self, level):
        return self.base_xp * level


class Element(object):
    def __init__(self, id):
        self.id = int(id) if id is not None else None
        self.type = ElementIds[self.id]

    @property
    def long_name(self):
        return self.type.name

    def __str__(self):
        return "{}".format(
            self.long_name,
        )

    def __repr__(self):
        return "<Element {}>".format(
            str(self)
        )

class Type(object):
    def __init__(self, id):
        self.id = id
        self.type = TypeIds[id]

    @property
    def long_name(self):
        return self.type.name

    def __str__(self):
        return "{}".format(
            self.long_name,
        )

    def __repr__(self):
        return "<Type {}>".format(
            str(self)
        )


class Attribute(object):
    def __init__(self, max, min, scale, owner):
        self.max = int(max)
        self.min = int(min)
        self.scale = int(scale)
        self.owner = owner

    def __str__(self):
        return "{min}/{max} * {scale}".format(
            min=self.min,
            max=self.max,
            scale=self.scale
        )

    def __repr__(self):
        return "<Attribute %s>" % str(self)

    def calc_for_level(self, level):
        lvl_calc = (level-1.0)/(self.owner.max_level-1.0)
        result =  self.min + (self.max - self.min) * lvl_calc ** self.scale
        return round(result)

class Monster(object):
    def __init__(self, **kwargs):
        self.load_data(**kwargs)

    def __str__(self):
        return "#{id} {name} ({rarity})".format(
            id=self.id,
            name=self.name.encode('utf8'),
            rarity=self.rarity*"*",
        )

    def __repr__(self):
        return "<Monster "+str(self)+">"

    def load_data(self, **kwargs):
        self.id = int(kwargs['id'])
        self.version = kwargs['version']

        self.rarity = kwargs['rarity']
        self.max_level = int(kwargs['max_level'])
        self.team_cost = int(kwargs['team_cost'])

        self.feed_xp = FeedXp(kwargs['feed_xp'])
        self.feed_xp_raw = int(kwargs['feed_xp'])

        self.xp_curve = XpCurve(kwargs['xp_curve'])
        self.xp_curve_raw = int(kwargs['xp_curve'])

        self.active_skill = ActiveSkill(0, 'UNSET ACTIVE SKILL', 0, 'UNSET ACTIVE SKILL NAME')
        self.active_skill_name = kwargs['active_skill']

        # self.awoken_skills_name = Awakening(kwargs['awoken_skills'])
        self.awoken_skills = kwargs['awoken_skills']

        self.leader_skill = LeaderSkill(
            'UNSET LEADER SKILL',
            'UNSET LEADER SKILL',
            [0, 0, 0, [None, None]]
        )
        self.leader_skill_name = kwargs['leader_skill']

        self.element = Element(kwargs['element'])
        self.element_id = int(kwargs['element'])
        self.element2 = Element(kwargs['element2'])
        self.element2_id = int(kwargs['element2']) if kwargs['element2'] else 0

        self.type = Type(kwargs['type'])
        self.type_id = int(kwargs['type']) if kwargs['type'] else 0
        self.type2 = Type(kwargs['type2'])
        self.type2_id = int(kwargs['type2']) if kwargs['type2'] else 0


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
            40,
            kwargs['image40_href'],
            kwargs['image40_size'],
            self,
        )

        self.image60 = Image(
            60,
            kwargs['image60_href'],
            kwargs['image60_size'],
            self,
        )

        self.jp_only = kwargs['jp_only']

class EvolutionComponent(object):
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

    def pretty(self, pad):
        return "Evolution: {base} -> {into}".format(
            base=str(pad.get_monster(self.monster_id)),
            into=str(pad.get_monster(self.evolves_to)),
        )

    def __repr__(self):
        return "<{str}>".format(
            str=str(self)
        )

    def load_materials(self, materials):
        self.materials = []
        for m_id, count in materials:
            material = EvolutionComponent(m_id, count, self)
            self.materials.append(material)

class EvolutionManager(BaseManager):
    identifier = "monster_id"
    can_find_many = True

    nested_list = True

    @property
    def model(self):
        return Evolution

    def build_obj(self, monster_id, **evo_data):
        return self.model(
            monster_id,
            evo_data['is_ultimate'],
            evo_data['evolves_to'],
            evo_data['materials'],
        )

    def get_by_evolves_to(self, evolves_to):
        objects =  filter(lambda obj: obj.evolves_to == evolves_to, self.objects)
        return objects

class LeaderSkillConstraint(object):
    def __init__(self, const_type=None, vals=None):
        self.const_type = ConstraintIds[const_type]
        self.load_vals(vals if vals else [None])

    def load_vals(self, vals):
        self.vals = []

        val_enum = ConstraintMap[self.const_type]
        for val in vals:
            self.vals.append(val_enum[val])

    def __str__(self):
        return "LSContraint: {pretty}".format(
            pretty=self.pretty(),
        )

    def pretty(self):
        return "{eot}:{val}".format(
            eot=self.const_type.value,
            val="".join(v.name for v in self.vals),
        )

    def __repr__(self):
        return "<{}>".format(str(self))

class LeaderSkillData(object):
    def __init__(self, hp=0, atk=0, rcv=0, *constraints):
        self.hp = hp
        self.atk = atk
        self.rcv = rcv
        self.load_constraints(constraints)

    def __str__(self):
        return "LSData: HPx{hp}/ATKx{atk}/RCVx{rcv} for {cnsts}".format(
            hp=self.hp,
            atk=self.atk,
            rcv=self.rcv,
            cnsts=" ".join([csnt.pretty() for csnt in self.constraints]),
        )

    def load_constraints(self, cnsts):
        self.constraints = []

        if not cnsts:
            self.constraints.append(LeaderSkillConstraint(None))

        for constraint in cnsts:
            c_type = constraint[0]
            vals = constraint[1:]

            lsc = LeaderSkillConstraint(c_type, vals)
            self.constraints.append(lsc)


class LeaderSkill(object):
    """
    has a name and effect, along with data, 
    data is an object that contains HP, ATK, and RCV values,
    plus a list of constraints to which type, or element, 
    of monsters it applies to
    """

    def __init__(self, name, effect, data=None):
        self.name = name
        self.effect = effect
        self.load_data(data)

    def __str__(self):
        return "LeaderSkill: {name}".format(
            name=self.name.encode('utf8')
        )

    def __repr__(self):
        return "<{}>".format(str(self))

    def load_data(self, data):
        if not data:
            data = []
        self.data = LeaderSkillData(*data)


class LeaderSkillManager(BaseManager):
    identifier = "name"
    has_default_object = True

    @property
    def model(self):
        return LeaderSkill

    def build_obj(self, **kwargs):
        return self.model(**kwargs)

    def get_for_monster(self, monster):
        ls = self.get_by_id(monster.leader_skill_name)
        return ls

    def get_default_object(self):
        return LeaderSkill("None", "No Effect", None)


class Awakening(object):
    def __init__(self, id, name, description):
        self.id = int(id)
        self.name = name
        self.description = description

    def __str__(self):
        return "Awakening: #{id} {name}".format(
            id=self.id,
            name=self.name.encode('utf8'),
        )

    def __repr__(self):
        return "<{str}>".format(
            str=str(self)
        )

class AwakeningManager(BaseManager):
    @property
    def model(self):
        return Awakening

    def build_obj(self, **kwargs):
        return self.model(
            kwargs['id'],
            kwargs['name'],
            kwargs['desc'],
        )

    def get_for_monster(self, monster):
        awakes = []
        for awk_id in monster.awoken_skills:
            awk = self.get_by_id(awk_id)
            awakes.append(awk)
        return awakes

class Food(object):
    def __init__(self, type, id, children):
        self.type = FoodIds[type]
        self.id = int(id)
        self.children = children

    def __str__(self):
        return "Food {type}#{id} {child}".format(
            type=self.type.name,
            id=self.id,
            child=self.children,
        )

    def __repr__(self):
        return "<{}>".format(str(self))

class FoodManager(BaseManager):
    nested_dict = True
    can_find_many = True

    @property
    def model(self):
        return Food
