from persistent import Persistent


class TagType(Persistent):

    all_instances = []

    def __init__(self, name, color):
        self.name = name
        self.color = color

        self.all_instances.append(self)

    @staticmethod
    def get_TagType(name, color=None):
        for i in TagType.all_instances:
            if i.name == name:
                return i
        return TagType(name, color)
