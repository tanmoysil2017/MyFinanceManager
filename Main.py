from pymongo import MongoClient
from MFDailyDetails import MFDailyDetails
from MFDailyDetailsCollection import MFDailyDetailsCollection


client = MongoClient()
db = client.pymongo_test

posts = db.posts
post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))
# "http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?frmdt=",text(today()-2,"dd-mmm-yyyy"), "&tp=1"))


import urllib3
wiki = "http://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?frmdt=12-11-2017&tp=1"
list_of_rates = []

http = urllib3.PoolManager()
r = http.request('GET', wiki)
if r.status == 200:
    str_data = r.data.decode("utf-8")
    total_found = 0
    for idx, line in enumerate(str_data.splitlines()):
        items = [i.strip() for i in line.split(';')]
        if len(items) > 1 and idx > 1:
            obj = MFDailyDetails()
            obj.load_value(items)
            list_of_rates.append(obj)
            total_found += 1

    MFDailyDetailsCollection(list_of_rates).execute()
    print(total_found)