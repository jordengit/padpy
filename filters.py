
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

