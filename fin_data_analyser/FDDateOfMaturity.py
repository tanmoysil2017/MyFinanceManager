from fin_data_analyser.DataAnalyser import *
from fin_manager_model.FrameworkHelper import *
from fin_manager_model.FixedDeposit import FixedDeposit
from fin_manager_model.ReportingEngine import ReportingEngine


class FDDateOfMaturity(DataRule):
    def __init__(self, reporting_currency='INR'):
        super(FDDateOfMaturity, self).__init__()
        self.reporting_currency = reporting_currency
        self.calculation_date = get_todays_date()

    def execute(self):
        re = ReportingEngine()
        re.reporting_currency = self.reporting_currency
        print('Fixed deposits matured before {}'.format(self.calculation_date))
        for ins in FixedDeposit.all_instances:
            if isinstance(ins, FixedDeposit) and ins.active and ins.fd_maturity_date <= self.calculation_date:
                print(ins.fd_maturity_date, '  ', ins.financial_org.type, '   ', ins.fd_id, '   ', ins.maturity_amount, ' ', ins.currency)
                self.amount += ins.maturity_amount
        print('Total {} {}'.format(self.amount, self.reporting_currency))


class FDCurrenctValue(DataRule):

    def __init__(self, reporting_currency='INR'):
        super(FDCurrenctValue, self).__init__()
        self.reporting_currency = reporting_currency
        self._calculation_date = get_todays_date()

    def execute(self):
        re = ReportingEngine()
        re.reporting_currency = self.reporting_currency
        print('Fixed deposits value on {}'.format(self._calculation_date))
        for ins in FixedDeposit.all_instances:
            if isinstance(ins, FixedDeposit) and ins.active:
                print(ins.fd_maturity_date, '  ', ins.financial_org.type, '   ', ins.fd_id, '   ', ins.calculate_value(reporting_engine=re, date=self._calculation_date), ' ', ins.currency)
                self.amount += ins.calculate_value(reporting_engine=re, date=self._calculation_date)

        print('Total {} {}'.format(self.amount, self.reporting_currency))


