from flask import Response, request
from flask_restful import Resource
from models.models import Project,Admin,User,Collab
from flask_httpauth import HTTPBasicAuth
import json

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(email, password):
    if not (email and password):
        return False
    ad = Admin.objects().to_json()
    res = json.loads(ad)
    for i in range(len(res)):
        if any(email == res[i]["email"] and password == res[i]["password"] for d in res):
            return True
        else:
            return False


class GetAllProjects(Resource):
    def get(self):
        proj = Project.objects().to_json()
        return Response(proj, mimetype="application/json", status=200)


class ModifyProject(Resource):
    def get(self):
        proj = Project.objects().to_json()
        return Response(proj, mimetype="application/json", status=200)

    @auth.login_required()
    def post(self):
        body = request.get_json(force=True)
        proj = Project(**body).save()
        id1 = proj.id
        return {'id': str(id1)}, 200

    @auth.login_required()
    def delete(self, id):
        proj = Project.objects.get(projectid=id).delete()
        return "Project Deleted Successfully!", 200

    @auth.login_required()
    def put(self, id):
        body = request.get_json(force=True)
        Project.objects.get(projectid=id).update(**body)
        return "Project Details Updated", 200


class UserDetails(Resource):
    def get(self):
        usr = User.objects().to_json()
        return Response(usr, mimetype="application/json", status=200)


class RegisterUser(Resource):
    def post(self):
        body = request.get_json(force=True)
        usr = User(**body)
        usr.save()
        uid = usr.id
        return {'id': str(uid)}, 200

    def put(self, id):
        body = request.get_json(force=True)
        User.objects.get(userid=id).update(**body)
        return 'User Details Updated Successfully!', 200


class AdminDetails(Resource):
    def get(self):
        adm = Admin.objects().to_json()
        return Response(adm, mimetype="application/json", status=200)


class RegisterAdmin(Resource):
    def post(self):
        body = request.get_json(force=True)
        adm = Admin(**body)
        adm.hash_password()
        adm.save()
        aid = adm.id
        return {'id': str(aid)}, 200

    @auth.login_required()
    def put(self, id):
        body = request.get_json(force=True)
        Admin.objects.get(admid=id).update(**body)
        return 'Admin Details Updated Successfully!', 200