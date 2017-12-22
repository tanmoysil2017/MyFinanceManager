from fin_data_importer.StaticData import *
from fin_manager_model.FixedDeposit import FixedDeposit
from fin_manager_model.FrameworkHelper import *
from fin_manager_model.MutualFunds import MutualFunds
import csv
from io import StringIO

reader = csv.reader(StringIO(fd), csv.excel)
FixedDeposit.load_data(reader)
reader = csv.reader(StringIO(nri_mf), csv.excel)
MutualFunds.load_data(reader)


for i in FixedDeposit.all_instances:
    print(i.date)
for i in MutualFunds.all_instances:
    print(i)