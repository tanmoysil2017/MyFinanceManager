from fin_data_importer.ImportFromGSheet import GSheetDownloader
from fin_data_analyser.DataAnalyser import *
from fin_data_analyser.TotalStocks import *
from fin_data_analyser.FDDateOfMaturity import *
from fin_data_analyser.MFValue import MFValue
from fin_data_analyser.BankAccountCurrentValue import BankAccountCurrentValue
from fin_data_analyser.TangibleAssetCurrentValue import TangibleAssetCurrentValue
import datetime
import babel.numbers


downloader = GSheetDownloader()
downloader.load_data()

analyser = DataAnalyser()

r1 = TotalStocks()
r1.reporting_currency = 'INR'
analyser.add_rule(r1)

r2 = FDDateOfMaturity()
r2.calculation_date = datetime.date(2018, 1, 1)
analyser.add_rule(r2)

r3 = FDCurrenctValue()
analyser.add_rule(r3)

r4 = MFValue()
analyser.add_rule(r4)

r5 = TangibleAssetCurrentValue()
analyser.add_rule(r5)

r6 = BankAccountCurrentValue()
analyser.add_rule(r6)

analyser.execute()

print('Stock: {}'.format(r1.amount))
print('Fixed deposit: {}'.format(r3.amount))
print('Mutual fund: {}'.format(r4.amount))
print('Tangible asset: {}'.format(r5.amount))
print('Bank accounts : {}'.format(r6.amount))
gt = r1.amount + r3.amount + r4.amount + r5.amount + r6.amount
print('Grand total: {}'.format(babel.numbers.format_currency(gt, r1.reporting_currency )))


# from fin_data_persistance.Persistance import *
# from fin_manager_model.OrgType import OrgType
# from fin_manager_model.FinancialOrg import FinancialOrg
#
# load_data()
# ############################################
# # ins = OrgType.all_instances
# # t1 = TagType('1', 'red')
# # t2 = TagType('2', 'blue')
# # bank = OrgType('BANK')
# # # for i in OrgType.all_instances:
# # #     print(i.type)
# # aib_joint = FinancialOrg('AIB-Joint Account', 'Ireland', 'N/A', bank)
# # aib_single = FinancialOrg('AIB-Single Account', 'Ireland', 'N/A', bank)
#
# #############################################
# save_data()
# db.close()
