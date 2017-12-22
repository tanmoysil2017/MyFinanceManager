
class ReportingEngine(object):

    all_instances = []

    def __init__(self):
        self.reporting_currency = 'INR'

        self.all_instances.append(self)


    def execute(self):
        from fin_manager_model.MoneyObject import MoneyObject

        for i in MoneyObject.all_instances:
            print(i.calculate_value(self))



