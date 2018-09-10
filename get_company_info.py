from flask import jsonify
from pymongo import MongoClient
from flask_restful import Resource



class GetCompanyInfo(Resource):
  def get(self):
    companyProfile = db.company_profile.find({});
    return jsonify({'result' : {"name": companyProfile[0]['name'], "address": companyProfile[0]['address']} })
