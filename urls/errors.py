class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class AdminAlreadyExistsError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

class DeleteProjectError(Exception):
    pass

class UpdateProjectError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

class NotAnAdminError(Exception):
    pass
errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "AdminAlreadyExistsError": {
         "message": "Admin with given id already exists",
         "status": 400
     },
     "UserAlreadyExistsError": {
         "message": "User already exists",
         "status": 403
     },
     "DeletingProjectError": {
         "message": "Not an authorized person to perform this",
         "status": 403
     },
     "UpdateProjectError": {
         "message": "Not an authorized person to perform this",
         "status": 400
     },
     "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}