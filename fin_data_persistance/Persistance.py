from fin_data_persistance.FINZODB import FINZODB
import transaction
import BTrees.OOBTree
from persistent import Persistent
from fin_manager_model.BankDeposit import BankDeposit
from fin_manager_model.FinancialOrg import FinancialOrg
from fin_manager_model.FixedDeposit import FixedDeposit
from fin_manager_model.FrameworkHelper import *
from fin_manager_model.MoneyObject import MoneyObject
from fin_manager_model.MutualFunds import MutualFunds
from fin_manager_model.OrgType import OrgType
from fin_manager_model.ReportingEngine import ReportingEngine
from fin_manager_model.Stock import Stock
from fin_manager_model.TagType import TagType

persistance_storage_path = './Data.fs'
db = FINZODB(persistance_storage_path)

list_persistant_object=['TagTypes', 'OrgType', 'MoneyObject', 'FinancialOrg',
                                                          'OrgType']

def populate_persistant_structure(dbroot=db.dbroot, lst=list_persistant_object):
    for item in lst:
        if item not in dbroot:
            dbroot[item] = []

def save_data():
    populate_persistant_structure()
    dbroot = db.dbroot

    dbroot['TagTypes'] = TagType.all_instances
    dbroot['OrgType'] = OrgType.all_instances
    dbroot['MoneyObject'] = MoneyObject.all_instances
    dbroot['FinancialOrg'] = FinancialOrg.all_instances

    transaction.commit()
    db.close()


def load_data():
    populate_persistant_structure()
    dbroot = db.dbroot

    OrgType.all_instances = dbroot['OrgType']
    TagType.all_instances = dbroot['TagTypes']
    MoneyObject.all_instances = dbroot['MoneyObject']
    FinancialOrg.all_instances = dbroot['FinancialOrg']

    transaction.commit()
