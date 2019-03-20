import pymongo
client = pymongo.MongoClient("mongodb://kunal:sahni1@ds125578.mlab.com:25578/ietmakeathon")
db = client['ietmakeathon']
tempdb = db.dht_sensor

def returnval():
    query = tempdb.find({})
    quer_list = [docs for docs in query]
    return [quer_list[-1]["temp"],quer_list[-1]["time"],quer_list[-1]["humidity"]]
