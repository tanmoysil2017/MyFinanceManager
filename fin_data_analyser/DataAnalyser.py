

class DataAnalyser:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def execute(self):
        for i in self.rules:
            i.execute()

class DataRule:

    def __init__(self):
        self.amount = 0.0

    def execute(self):
        pass