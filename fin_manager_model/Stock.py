from fin_manager_model.MoneyObject import MoneyObject
from fin_manager_model.ReportingEngine import ReportingEngine
from fin_manager_model.OrgType import OrgType
from fin_manager_model.FrameworkHelper import *


class Stock(MoneyObject):

    def __init__(self):
        super(Stock, self).__init__()
        self.unit = 0.0
        self.stock_name = ''
        self.stock_id = ''

    def _multiplier(self, reporting_engine: ReportingEngine, caldate: date):
        if self.value:
            return (stock_price(self.stock_id) * self.unit)/self.value

        return stock_price(self.stock_id) * self.unit

    @staticmethod
    def load_data(data_stream, parm1, parm2):
        prefix = ''
        for i in data_stream:
            if len(i) > 2:
                fd = Stock()
                fd.unit = parse_str_to_float(i[1])
                fd.stock_name = parm1
                fd.currency = parm2
                fd.stock_id = i[0]


