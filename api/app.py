from flask import Flask, Blueprint
from flask_restful import Api, url_for
from get_company_info import GetCompanyInfo

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(GetCompanyInfo, '/company-info')
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)
