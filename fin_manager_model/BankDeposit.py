from fin_manager_model.MoneyObject import MoneyObject
from fin_manager_model.ReportingEngine import ReportingEngine
from fin_manager_model.OrgType import OrgType
from fin_manager_model.FrameworkHelper import *

class BankDeposit(MoneyObject):

    def __init__(self):
        super(BankDeposit, self).__init__()
        
    def _multiplier(self, reporting_engine:ReportingEngine, date:date):
        return super(BankDeposit, self)._multiplier(reporting_engine, date)

    @staticmethod
    def load_data(data_stream, parm1):
        prefix = ''
        for i in data_stream:
            if len(i) > 2:
                fd = BankDeposit()
                fd.active = True
                fd.date = get_todays_date()
                fd.value = parse_str_to_float(i[2])
                fd.description = prefix + ' ' + i[1]
                fd.currency = parm1
                fd.tag_types = [] #TagType.get_TagType('FixedDeposit')
                fd.financial_org = OrgType.get_OrgType(prefix)
            else:
                prefix = i[0]


