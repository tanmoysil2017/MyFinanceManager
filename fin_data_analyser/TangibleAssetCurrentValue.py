from fin_data_analyser.DataAnalyser import *
from fin_manager_model.FrameworkHelper import *
from fin_manager_model.TangibleAsset import TangibleAsset
from fin_manager_model.ReportingEngine import ReportingEngine


class TangibleAssetCurrentValue(DataRule):
    def __init__(self, reporting_currency='INR'):
        super(TangibleAssetCurrentValue, self).__init__()
        self.reporting_currency = reporting_currency
        self.calculation_date = get_todays_date()

    def execute(self):
        re = ReportingEngine()
        re.reporting_currency = self.reporting_currency
        for ins in TangibleAsset.all_instances:
            if isinstance(ins, TangibleAsset) and ins.active:
                self.amount += ins.calculate_value(reporting_engine=re, date=self.calculation_date)

        print('Total tangible asset {} {}'.format(self.amount, self.reporting_currency))