
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

    def by_rarity(self, rarity):
        return filter(lambda m: m.rarity == int(rarity), self.objects)

    def by_team_cost(self, cost):
        return filter(lambda m: m.team_cost == int(cost), self.objects)

    def by_active_skill(self, name):
        return filter(lambda m: m.active_skill.name == name, self.objects)

