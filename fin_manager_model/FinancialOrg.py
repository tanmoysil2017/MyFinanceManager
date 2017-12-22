from persistent import Persistent

class FinancialOrg(Persistent):

    all_instances = {}

    def __init__(self, name, location, agent, org_type):
        self.name = name
        self.location = location
        self.agent = agent
        self.org_type = org_type

        self.all_instances.append(self)

