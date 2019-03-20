import pymongo
client = pymongo.MongoClient("mongodb://kunal:sahni1@ds125578.mlab.com:25578/ietmakeathon")
db = client['ietmakeathon']

raindb = db.rain_sensor

def returnval():
    query = raindb.find({})
    quer_list = [docs for docs in query]
    return quer_list[-1]["status"],quer_list[-1]["time"]
