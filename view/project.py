from flask import Response, request, Flask
from flask_restful import Resource
from models.models import Project, Admin, User, Collab
from flask_httpauth import HTTPBasicAuth
import json
from urls.errors import *
from flask_mail import Mail, Message

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tt1411509@gmail.com'
app.config['MAIL_PASSWORD'] = 'test@test@123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


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
        try:
            body = request.get_json(force=True)
            proj = Project(**body).save()
            response = proj.id
            return {'id': str(response)}, 200
        except Exception as e:
            raise NotAnAdminError("Project Id already exists!")

    @auth.login_required()
    def delete(self, id):
        try:
            proj = Project.objects.get(projectid=id).delete()
            return "Project Deleted Successfully!", 200
        except Exception as e:
            raise NotAnAdminError("Project Id not found!")

    @auth.login_required()
    def put(self, id):
        try:
            body = request.get_json(force=True)
            Project.objects.get(projectid=id).update(**body)
            return "Project Details Updated", 200
        except Exception as e:
            raise NotAnAdminError("Project can't be found for updation!")


class UserDetails(Resource):
    def get(self):
        try:
            usr = User.objects().to_json()
            return Response(usr, mimetype="application/json", status=200)
        except Exception as e:
            raise UnauthorizedError("Not an authorizeed person!")


class RegisterUser(Resource):
    def post(self):
        try:
            body = request.get_json(force=True)
            usr = User(**body)
            usr.save()
            uid = usr.id
            return {'id': str(uid)}, 200
        except:
            return "Username should be unique", 500


class UpdateUser(Resource):
    def put(self, id):
        try:
            body = request.get_json(force=True)
            User.objects.get(userid=id).update(**body)
            return 'User Details Updated Successfully!', 200
        except Exception as E:
            raise UnauthorizedError("User does not Exist!")


class AdminDetails(Resource):
    def get(self):
        try:
            adm = Admin.objects().to_json()
            return Response(adm, mimetype="application/json", status=200)
        except Exception as e:
            raise UnauthorizedError("Not an authorised person!")


class RegisterAdmin(Resource):
    def post(self):
        try:
            body = request.get_json(force=True)
            adm = Admin(**body)
            adm.hash_password()
            adm.save()
            aid = adm.id
            return {'id': str(aid)}, 200
        except (UnauthorizedError, AdminAlreadyExistsError):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError("Id Already Exists! Admin ID should be unique.")


class UpdateAdmin(Resource):
    @auth.login_required()
    def put(self, id):
        try:
            body = request.get_json(force=True)
            Admin.objects.get(admid=id).update(**body)
            return 'Admin Details Updated Successfully!', 200
        except Exception as E:
            raise UnauthorizedError("Admin doesnot Exist!")


class ProjectCollab(Resource):
    def post(self):
        try:
            body = request.get_json(force=True)
            proj_collab = Collab(**body)
            proj_collab.save()
        except Exception as e:
            raise "Project does not exists!"
        msg = Message('Project Collab', sender='tt1411509@gmail.com', recipients=[body["admin_email"]])
        msg.body = "Hello sir/ma'am, I would like to collaborate with you in the mentioned project.\n" + str(
            body["project_id"]) + str(body["project_name"]) + "\nThank You!"
        mail.send(msg)
        return "Email Sent to admin regarding project collaboration!", 200
