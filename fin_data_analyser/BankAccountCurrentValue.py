from fin_data_analyser.DataAnalyser import *
from fin_manager_model.FrameworkHelper import *
from fin_manager_model.BankDeposit import BankDeposit
from fin_manager_model.ReportingEngine import ReportingEngine


class BankAccountCurrentValue(DataRule):
    def __init__(self, reporting_currency='INR'):
        super(BankAccountCurrentValue, self).__init__()
        self.reporting_currency = reporting_currency
        self.calculation_date = get_todays_date()

    def execute(self):
        re = ReportingEngine()
        re.reporting_currency = self.reporting_currency
        for ins in BankDeposit.all_instances:
            if isinstance(ins, BankDeposit) and ins.active:
                self.amount += ins.calculate_value(reporting_engine=re, date=self.calculation_date)

        print('Total Bank account asset {} {}'.format(self.amount, self.reporting_currency))

