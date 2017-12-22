from fin_manager_model.MoneyObject import MoneyObject
from fin_manager_model.ReportingEngine import ReportingEngine
from fin_manager_model.FrameworkHelper import *
from fin_manager_model.OrgType import OrgType
from fin_manager_model.TagType import TagType


class FixedDeposit(MoneyObject):

    def __init__(self):
        super(FixedDeposit, self).__init__()
        self.fd_maturity_date = None
        self.fd_id = ''
        self.interest = 0.0
        self.maturity_amount = 0.0

    def _multiplier(self, reporting_engine: ReportingEngine, caldate: date):
        if (not self.active and self.maturity_amount) or (caldate >= self.fd_maturity_date and self.maturity_amount):
            return self.maturity_amount / self.value

        span = caldate - self.date
        years = span.days / 365
        if self.value:
            return compound_interest(self.value, self.interest, 4, years) / self.value

        return compound_interest(self.value, self.interest, 4, years)

    @staticmethod
    def load_data(data_stream, parm1='PostOffice'):
        for i in data_stream:
            if parm1 == 'FixedDeposit':
                if len(i) > 2:
                    fd = FixedDeposit()
                    fd.active = parse_str_to_boolean(i[0])
                    fd.date = parse_str_to_date(i[1])
                    fd.value = parse_str_to_float(i[5])
                    fd.description = ''
                    fd.currency = 'INR'
                    fd.tag_types = TagType.get_TagType('FixedDeposit')
                    fd.financial_org = OrgType.get_OrgType(i[3])
                    fd.fd_maturity_date = parse_str_to_date(i[2])
                    fd.fd_id = i[4]
                    fd.interest = parse_str_to_float(i[6]) / 100
                    fd.maturity_amount = parse_str_to_float(i[7])
            elif parm1 == 'PostOffice':
                if len(i) > 2:
                    fd = FixedDeposit()
                    fd.active = parse_str_to_boolean(i[0])
                    fd.date = parse_str_to_date(i[3])
                    fd.value = parse_str_to_float(i[4])
                    fd.description = i[2]
                    fd.currency = 'INR'
                    fd.tag_types = TagType.get_TagType('PostOffice')
                    fd.financial_org = OrgType.get_OrgType(i[1])
                    fd.fd_maturity_date = parse_str_to_date(i[5])
                    fd.fd_id = i[2]
                    fd.maturity_amount = parse_str_to_float(i[6])
                    # Now calculate interest rate
                    span = fd.fd_maturity_date - fd.date
                    years = span.days / 365
                    fd.interest = get_compund_interest_rate(fd.value, fd.maturity_amount, 4, years)
