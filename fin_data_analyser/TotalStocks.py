from fin_data_analyser.DataAnalyser import *
from fin_manager_model.Stock import Stock
from fin_manager_model.ReportingEngine import ReportingEngine

class TotalStocks(DataRule):
    def __init__(self, reporting_currency='INR'):
        super(TotalStocks, self).__init__()
        self.reporting_currency = reporting_currency

    def execute(self):
        re = ReportingEngine()
        re.reporting_currency = self.reporting_currency
        amount = 0.0
        for ins in Stock.all_instances:
            if isinstance(ins, Stock):
                amount += ins.calculate_value(reporting_engine=re)

        print('Total Stock Price {} {}'.format(amount, self.reporting_currency))
        self.amount = amount


