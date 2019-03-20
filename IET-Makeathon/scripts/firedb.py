import pymongo
client = pymongo.MongoClient("mongodb://kunal:sahni1@ds125578.mlab.com:25578/ietmakeathon")
db = client['ietmakeathon']
firedb = db.fire_sensor

def returnval():
    query = firedb.find({})
    quer_list = [docs for docs in query]
    return quer_list[-1]["status"],quer_list[-1]["time"]
