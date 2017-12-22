from persistent import Persistent


class OrgType(Persistent):

    all_instances = []

    def __init__(self, type):
        self.type = type
        self.all_instances.append(self)

    @staticmethod
    def get_OrgType(type):
        for i in OrgType.all_instances:
            if i.type == type:
                return i

        return OrgType(type)