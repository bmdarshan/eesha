from flask import jsonify
from pymongo import MongoClient
from flask_restful import Resource

client = MongoClient("mongodb://heroku_jdf17hjj:s77scqp3e4kvhgub6su4g5bu12@ds251002.mlab.com:51002/heroku_jdf17hjj")
db = client.heroku_jdf17hjj

class GetCompanyInfo(Resource):
  def get(self):
    companyProfile = db.company_profile.find({});
    return jsonify({'result' : {"name": companyProfile[0]['name'], "address": companyProfile[0]['address']} })
