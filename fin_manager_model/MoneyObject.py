from fin_manager_model.FrameworkHelper import *
from fin_manager_model.ReportingEngine import ReportingEngine
from persistent import Persistent


class MoneyObject(Persistent):

    all_instances = []

    def __init__(self):
        self.date = get_todays_date()
        self.value = 0.0
        self.active = True
        self.description = ''
        self.currency = 'INR'
        self.tag_types = []
        self.financial_org = None

        self.all_instances.append(self)

    def _multiplier(self, reporting_engine:ReportingEngine, date:date):
        return 1

    def calculate_value(self, reporting_engine:ReportingEngine, date = get_todays_date()):
        currency_conv = 1.0
        if reporting_engine.reporting_currency != self.currency:
            currency_conv = get_converted_currency_rate(self.currency, reporting_engine.reporting_currency)
        if self.value:
            return self.value * self._multiplier(reporting_engine, date) * currency_conv

        return self._multiplier(reporting_engine, date) * currency_conv

    @staticmethod
    def load_data(data_stream, parm1, parm2):
        pass

    @staticmethod
    def save_data(data_stream):
        pass
