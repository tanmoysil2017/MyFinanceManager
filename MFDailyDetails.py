import datetime
from dateutil import parser
import jsonpickle
import json
import unicodedata
from MDBObject import MDBObject


class MFDailyDetails(MDBObject):

    def __init__(self, json_data = {}):
        if json_data != {}:
            self.SchemeCode = json_data['SchemeCode']
            self.SchemeName = json_data['SchemeName']
            self.NetAssetValue = json_data['NetAssetValue']
            self.RepurchasePrice = MFDailyDetails.str_to_float(json_data['RepurchasePrice'])
            self.SalePrice = MFDailyDetails.str_to_float(json_data['SalePrice'])
            self.Date = MFDailyDetails.str_to_datetime(json_data['Date'])
        else:
            self.SchemeCode = ''
            self.SchemeName = ''
            self.NetAssetValue = ''
            self.RepurchasePrice = 0.0
            self.SalePrice = 0.0
            self.Date = datetime.datetime.utcnow()

        self.temp1 = 0.0
        self.temp2 = 0.0
        self.temp3 = 0.0

    def load_value(self, lst):
        self.SchemeCode = lst[0]
        self.SchemeName = lst[1]
        self.NetAssetValue = lst[2]
        self.RepurchasePrice = MFDailyDetails.str_to_float(lst[3])
        self.SalePrice = MFDailyDetails.str_to_float(lst[4])
        self.Date = MFDailyDetails.str_to_datetime(lst[5])

    def encode_to_json(self):
        json_data = super(MFDailyDetails, self).encode_to_json()
        json_data['SchemeCode'] = self.SchemeCode
        json_data['SchemeName'] = self.SchemeName
        json_data['NetAssetValue'] = self.NetAssetValue
        json_data['RepurchasePrice'] = self.RepurchasePrice
        json_data['SalePrice'] = self.SalePrice
        json_data['Date'] = self.Date.isoformat()

        return json_data

    def populate_key(self):
        return self.SchemeCode + str(self.Date)[:19]



    @staticmethod
    def str_to_float(str):
        ret = 0.0
        if str != 'N.A.':
            ret = float(str)
        return ret

    @staticmethod
    def str_to_datetime(str, default_value = datetime.datetime.utcnow()):
        ret = default_value
        if str != 'N.A.':
            ret = parser.parse(str)
        return ret


