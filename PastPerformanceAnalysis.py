from TimeFrame import TimeFrame
from MFDailyDetailsCollection import MFDailyDetailsCollection
import datetime


class PastPerformanceAnalysis():
    def __init__(self):
        self.number_of_months = 12
        self.investing_amount = 10000
        self.number_of_top_mf = 200

    def execute(self):
        # Download today's data:
        collection_of_rate = MFDailyDetailsCollection()
        collection_of_rate.download_from_internet(datetime.date.today())
        time_frame = TimeFrame()
        time_frame.calculate_dates(self.number_of_months)

        for item in collection_of_rate.instances:
                past_results = self.find_instances_from_db(item.SchemeCode)
                if len(past_results) >= self.number_of_months:
                    number_of_unit = 0.0
                    for i in range(0, self.number_of_months-1):
                        if past_results[i].RepurchasePrice == 0.0:
                            break
                        number_of_unit += (self.investing_amount / past_results[i].RepurchasePrice)
                    item.temp1 = number_of_unit
                    item.temp2 = number_of_unit * item.SalePrice
                    item.temp3 = item.temp2 - (self.number_of_months * self.investing_amount)

        collection_of_rate.instances.sort(key = lambda c: c.temp3, reverse=True)
        collection_of_rate.instances = collection_of_rate.instances[:self.number_of_top_mf]

        for item in collection_of_rate.instances:
            print(item.SchemeName, ',', item.SchemeCode, ',', item.temp3)

            # for i in range(0, self.number_of_months-1):

            # for period in time_frame.periods:
            #     pass
        # time_frame = TimeFrame()
        # time_frame.calculate_dates(12)
        # for i in time_frame.periods:
        #     print (i)


    def download_past_performance_data(self):
        time_frame = TimeFrame()
        time_frame.calculate_dates(12)
        for period in time_frame.periods:
            print('Downloding data for date ' + str(period))
            daily_colelction = MFDailyDetailsCollection()
            daily_colelction.download_from_internet(period)
            daily_colelction.execute()

    def find_instances_from_db(self, strCode):
        collection_of_rate = MFDailyDetailsCollection()
        collection_of_rate.find_from_SchemeCode(strCode)
        return collection_of_rate.instances

if __name__ == '__main__':
    a = PastPerformanceAnalysis()
    a.execute()