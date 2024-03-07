
from flask import Blueprint, request,make_response
from app.cache import getNextValue
import pymongo
import json

user_bp = Blueprint('users', __name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
battle_db = myclient["manage"]
users = battle_db['users']


@user_bp.route('/users')
def getUsers():
    [current,pageSize] = json.loads(request.args.get('range'))
    [field,order] =  json.loads(request.args.get('sort'))
    order_int = 1 if order == 'ASC'else 0
    usersdata = users.find({}).sort(field, order_int).limit(pageSize).skip(
        (current - 1) * pageSize)
    res = {}
    res['data'] = list(usersdata)
    res['total'] = users.count_documents({})
    return res
    
    

@user_bp.route('/users/<id>')
def getUsersById(id):
    user = users.find_one({"id":int(id)})
    return dict(user)
    
   

@user_bp.route('/users/<id>',methods=['DELETE'])
def deleteUsers(id):
    users.delete_one({"_id":id})
    return make_response('',200)
   

@user_bp.route('/users',methods=['DELETE'])
def deleteManyUsers():
    filter =  json.loads(request.args.get('filter'))
    ids = filter['id']
    users.delete_many({'_id': {"$in":ids}})
    return make_response([],200)
   
   
@user_bp.route('/users/<id>',methods=['PUT'])
def updataUsers(id):
    req_data = request.json
    users.update_one({"id":int(id)},{"$set":req_data})
    data = users.find_one({"id":int(id)})
    return dict(data)

@user_bp.route('/users',methods=['POST'])
def addUsers():
    req_data = request.json
    username =  req_data['username']
    _id = getNextValue("teamlibraryId")
    users.insert_one({"id":_id,"_id":_id,"username":username,"password":"123456"})
    return make_response({"id":_id,"_id":_id,"username":username,"password":"123456"},200)
    
  