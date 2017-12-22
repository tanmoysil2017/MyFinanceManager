
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'MyFinanceManager'

class GSheetDownloader:

    spreadsheetId = '1rHvMPfpEC8JQ3S2xcOIC8U2zCj0LtQArn_CQmmLmr94'

    def __init__(self):
        credentials = GSheetDownloader.get_credentials()
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        self.service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)

    def get_data(self, range_name, func, parm1=None, parm2=None):
        if self.service:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheetId, range=range_name).execute()
            if result:
                if parm1 is None and parm2 is not None:
                    func(result.get('values', []))
                elif parm2 is None:
                    func(result.get('values', []), parm1)
                else:
                    func(result.get('values', []), parm1, parm2)


    @staticmethod
    def get_credentials():
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'sheets.googleapis.com-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else: # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    def load_data(self):
        from fin_manager_model.MutualFunds import MutualFunds
        from fin_manager_model.FixedDeposit import FixedDeposit
        from fin_manager_model.BankDeposit import BankDeposit
        from fin_manager_model.Stock import Stock
        from fin_manager_model.TangibleAsset import TangibleAsset

        print('Reading data from GSheet...')
        self.get_data('MF_NRI!A2:H', MutualFunds.load_data, True)
        self.get_data('MF!A2:H', MutualFunds.load_data, False)
        self.get_data('FixedDeposit!A2:H', FixedDeposit.load_data, 'FixedDeposit')
        self.get_data('PostOffice!A2:G', FixedDeposit.load_data, 'PostOffice')
        self.get_data('European Savings!A4:C7', BankDeposit.load_data, 'EUR')
        self.get_data('European Savings!A8:C8', Stock.load_data, 'Workday', 'USD')
        self.get_data('Total!A7:C7', TangibleAsset.load_data, 'INR')

        print('Reading Complete from GSheet...')


def main():
    gs = GSheetDownloader()
    gs.load_data()


if __name__ == '__main__':
    main()