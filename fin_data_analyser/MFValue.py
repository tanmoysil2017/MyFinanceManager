from fin_data_analyser.DataAnalyser import *
from fin_manager_model.FrameworkHelper import *
from fin_manager_model.MutualFunds import MutualFunds
from fin_manager_model.ReportingEngine import ReportingEngine


class MFValue(DataRule):
    def __init__(self, reporting_currency='INR'):
        super(MFValue, self).__init__()
        self.reporting_currency = reporting_currency
        self.calculation_date = get_todays_date()

    def execute(self):
        re = ReportingEngine()
        re.reporting_currency = self.reporting_currency
        print('Fixed deposits matured before {}'.format(self.calculation_date))
        for ins in MutualFunds.all_instances:
            if isinstance(ins, MutualFunds) and ins.active:
                self.amount += ins.calculate_value(reporting_engine=re, date=self.calculation_date)
                print(ins.mf_name, '  ', ins.unit, '   ', ins.calculate_value(reporting_engine=re, date=self.calculation_date))

        print('Total {} {}'.format(self.amount, self.reporting_currency))