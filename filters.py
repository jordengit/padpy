
class MonsterFilter(object):
    def __init__(self, monsters):
        self.objects = monsters

    def by_element(self, element):
        return filter(lambda m: m.element.type == element, self.objects)

    def by_element2(self, element):
        return filter(lambda m: m.element2.type == element, self.objects)
    
    def by_type(self, type):
        return filter(lambda m: m.type.type == type, self.objects)

    def by_type2(self, type):
        return filter(lambda m: m.type2.type == type, self.objects)
    
    def by_type3(self, type):
	return filter(lambda m: m.typ3.type == type, self.objects)

    def by_rarity(self, rarity):
        return filter(lambda m: m.rarity == int(rarity), self.objects)

    def by_team_cost(self, cost):
        return filter(lambda m: m.team_cost == int(cost), self.objects)

    def by_active_skill(self, name):
        return filter(lambda m: m.active_skill.name == name, self.objects)

    def by_leader_skill(self, name):
        return filter(lambda m: m.leader_skill.name == name, self.objects)

    def by_max_level(self, level):
        return filter(lambda m: m.max_level == int(level), self.objects)

    def by_jp_only(self, jp_only):
        return filter(lambda m: m.jp_only == bool(jp_only), self.objects)

