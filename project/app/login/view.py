from flask import Blueprint, request,make_response
from app.cache import getNextValue
import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
battle_db = myclient["manage"]
users = battle_db['users']



login_bp = Blueprint('login', __name__)



@login_bp.route('/login',methods=['POST'])
def getById():
    reqData = request.json
    username = reqData['username']
    password = reqData['password']
    data = users.find_one({"password":password,"username":username})
    if data!=None:
        return make_response(dict(data),200)
    else:
        return make_response("账号或者密码错误！",402)