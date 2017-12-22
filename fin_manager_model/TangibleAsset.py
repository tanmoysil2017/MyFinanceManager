from fin_manager_model.MoneyObject import MoneyObject
from fin_manager_model.ReportingEngine import ReportingEngine
from fin_manager_model.FrameworkHelper import *
from fin_manager_model.OrgType import OrgType
from fin_manager_model.TagType import TagType


class TangibleAsset(MoneyObject):

    def __init__(self):
        super(TangibleAsset, self).__init__()

    def _multiplier(self, reporting_engine: ReportingEngine, caldate: date):
        return 1.0

    @staticmethod
    def load_data(data_stream, parm1='INR'):
        for i in data_stream:
            ins = TangibleAsset()
            ins.value = parse_str_to_float(i[2])
            ins.currency = parm1
            ins.description = i[1]
