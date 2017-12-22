from MFDailyDetails import MFDailyDetails
from MongoInterface import *
from dateutil.relativedelta import *
import datetime
import json
import pymongo

class MFDailyDetailsCollection():

    def __init__(self, instances = None):
        self.instances = instances
        self.download_date = datetime.date.today()

    def execute(self, download_date=datetime.date.today(), use_mongo=False):
        if use_mongo:
            mongo = MongoInterface()
            for i in self.instances:
                mongo.insert(i, DailyRateCollectionName)
        else:
            if not self.instances:
                self.download_from_internet(download_date)

    def find_from_SchemeCode(self, code, use_mongo=False):
        if use_mongo:
            mongo = MongoInterface()
            items = mongo.search({'SchemeCode': code}, DailyRateCollectionName).sort('date',pymongo.DESCENDING)
            self.instances = []
            for item in items:
                self.instances.append(MFDailyDetails(item))
        elif self.instances:
            for ins in self.instances:
                if ins.SchemeCode == code:
                    return ins.SalePrice

            print('No NAV found for {}'.format(code))
            return 0.0

    def download_from_internet(self, download_date):
        import urllib3
        date_format = download_date.strftime('%m-%d-%Y')

        wiki = "http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?frmdt=" + date_format + "&tp=1"
        list_of_rates = []

        http = urllib3.PoolManager()
        r = http.request('GET', wiki)
        if r.status == 200:
            str_data = r.data.decode("utf-8")
            total_found = 0
            if len(str_data.splitlines()) < 1000:
                print(str(download_date) + 'less data found')
                return self.download_from_internet(download_date + relativedelta(days=-1))
            for idx, line in enumerate(str_data.splitlines()):
                items = [i.strip() for i in line.split(';')]
                if len(items) > 1 and idx > 1:
                    obj = MFDailyDetails()
                    obj.load_value(items)
                    list_of_rates.append(obj)
                    total_found += 1

        self.instances = list_of_rates
        self.download_date = download_date