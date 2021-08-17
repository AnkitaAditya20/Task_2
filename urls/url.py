from view.project import GetAllProjects, ModifyProject, UserDetails, AdminDetails, RegisterAdmin, RegisterUser, ProjectCollab, UpdateAdmin, UpdateUser

def initialize_routes(api):
    api.add_resource(GetAllProjects, '/projects')
    api.add_resource(ModifyProject, '/modifyproject')
    api.add_resource(UserDetails, '/users')
    api.add_resource(AdminDetails, '/admin')
    api.add_resource(RegisterAdmin, '/registeradmin')
    api.add_resource(UpdateAdmin, '/updateadmin/<id>')
    api.add_resource(RegisterUser, '/registeruser')
    api.add_resource(UpdateUser, '/updateuser/<id>')
    api.add_resource(ProjectCollab, '/collab')