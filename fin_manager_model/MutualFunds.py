from fin_manager_model.MoneyObject import MoneyObject
from fin_manager_model.ReportingEngine import ReportingEngine
from fin_manager_model.FrameworkHelper import *
from fin_manager_model.TagType import TagType
from fin_manager_model.OrgType import OrgType

class MutualFunds(MoneyObject):

    def __init__(self):
        super(MutualFunds, self).__init__()
        self.unit = 0.0
        self.mf_id = ''
        self.mf_name = ''

    def _multiplier(self, reporting_engine: ReportingEngine, caldate: date):
        if self.value:
            return (self.unit * mf_nav_value(self.mf_id, caldate))/self.value

        return self.unit * mf_nav_value(self.mf_id, caldate)

    @staticmethod
    def load_data(data_stream, nri=True):
        if nri:
            for i in data_stream:
                if len(i) >= 7:
                    mf = MutualFunds()
                    mf.active = parse_str_to_boolean(i[0])
                    mf.date = parse_str_to_date(i[3])
                    mf.value = parse_str_to_float(i[5])
                    mf.description = i[4]
                    mf.currency = 'INR'
                    mf.tag_types = TagType.get_TagType('NRI_FD')
                    mf.financial_org = OrgType.get_OrgType(parse_str_to_mf_name(i[2]))

                    mf.unit = parse_str_to_float(i[7])
                    mf.mf_id = i[1]
                    mf.mf_name = i[2]
        else:
            for i in data_stream:
                if len(i) >= 7:
                    mf = MutualFunds()
                    mf.active = parse_str_to_boolean(i[0])
                    mf.date = parse_str_to_date(i[3])
                    mf.value = parse_str_to_float(i[5])
                    mf.description = i[4]
                    mf.currency = 'INR'
                    mf.tag_types = TagType.get_TagType('Kalpana_FD')
                    mf.financial_org = OrgType.get_OrgType(parse_str_to_mf_name(i[2]))

                    mf.unit = parse_str_to_float(i[7])
                    mf.mf_id = i[1]
                    mf.mf_name = i[2]
