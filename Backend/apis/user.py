from flask_restplus import Namespace, Resource, fields

api = Namespace('user', description='User related operations')

user = api.model('user', {
    'id': fields.Integer(readonly=True, description='The users unique identifier'),
    'firstName': fields.String(required=True, description='The users first name'),
    'lastName' : fields.String(required=True, description='The users last name')
})

USERS = [
    {'id': 1, 'firstName': 'External', 'lastName': 'Stub'},
    {'id': 2, 'firstName': 'Mule', 'lastName': 'Soft'},
    {'id': 3, 'firstName': 'Any', 'lastName': 'Point'},
    {'id': 4, 'firstName': 'Post', 'lastName': 'Man'},
    {'id': 5, 'firstName': 'Smart', 'lastName': 'Stub'},

]

@api.route('/')
class UserList(Resource):
    '''Shows a list of all users, and lets you post new users?'''
    @api.doc('list_users')
    @api.marshal_list_with(user)
    def get(self):
        '''List all users'''
        return USERS

@api.route('/<id>')
@api.param('id', 'The users unique identifier')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get_user')
    @api.marshal_with(user)
    def get(self, id):
        '''Fetch a user given its identifier'''
        for user in USERS:
            if user['id'] == id:
                return user
        api.abort(404)