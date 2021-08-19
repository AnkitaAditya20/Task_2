from view.project import GetAllProjects, ModifyProject, UserDetails, AdminDetails, RegisterAdmin, RegisterUser

def initialize_routes(api):
    api.add_resource(GetAllProjects, '/projects')
    api.add_resource(ModifyProject, '/modifyproject')
    api.add_resource(UserDetails, '/users')
    api.add_resource(AdminDetails, '/admin')
    api.add_resource(RegisterAdmin, '/registeradmin/<id>')
    api.add_resource(RegisterUser, '/registeruser/<id>')