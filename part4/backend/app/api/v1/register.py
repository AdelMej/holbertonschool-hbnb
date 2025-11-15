from flask_restx import Namespace, Resource, fields
from app.services import facade
from app.utils.password_validator import verify_password
import validators

api = Namespace('register', description="User registration")

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'id': fields.String(
        readonly=True,
        description='The unique identifier of a user'
    ),
    'first_name': fields.String(
        required=True,
        description='First name of the user'
    ),
    'last_name': fields.String(
        required=True,
        description='Last name of the user'
    ),
    'email': fields.String(
        required=True,
        description='Email of the user'
    ),
    'password': fields.String(
        required=True,
        description='The password of the user'
    )
})


@api.route('/')
class register(Resource):

    @api.expect(user_model, validate=True)
    @api.response(400, 'Invalid Input')
    @api.response(400, 'Invalid email')
    @api.response(400, 'Invalid password')
    @api.doc(description="registration route for normal user")
    def post(self):
        user_data = api.payload

        # check email uniqueness check
        if facade.get_user_by_email(user_data['email']):
            return {'error': 'Email already registered'}, 400

        # Verify input data
        if (
            user_data['first_name'] == ''
            or user_data['last_name'] == ''
            or user_data['email'] == ''
        ):
            return {'error': 'Invalid input data'}, 400

        # verify email format
        if not validators.email(user_data['email']):
            return {'error': 'Invalid email'}, 400

        # verify password
        success, message = verify_password(user_data["password"])
        if not success:
            return {'error': message}, 400

        facade.create_user(user_data)
        return {"message": 'registration successful'}, 201
