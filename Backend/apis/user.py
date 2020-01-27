from flask_restplus import Namespace, Resource, fields

api = Namespace('Users', description='User related operations')

user = api.model('user', {
    'id': fields.Integer(readonly=True, description='The user unique identifier'),
    'firstName': fields.String(required=True, description='The user first name'),
    'lastName' : fields.String(required=True, description='The user last name')
})


class UserDAO(object):
    def __init__(self):
        self.counter = 0
        self.User = []

    def get(self, id):
        for usr in self.User:
            if usr['id'] == id:
                return usr
        api.abort(404, "User {} doesn't exist".format(id))

    def create(self, data):
        usr = data
        usr['id'] = self.counter = self.counter + 1
        self.User.append(usr)
        return usr

    def update(self, id, data):
        usr = self.get(id)
        usr.update(data)
        return usr

    def delete(self, id):
        usr = self.get(id)
        self.User.remove(usr)


USERS = UserDAO()
USERS.create({'firstName': 'External', 'lastName': 'Stub'})
USERS.create({'firstName': 'Mule', 'lastName': 'Soft'})
USERS.create({'firstName': 'Any', 'lastName': 'Point'})
USERS.create({'firstName': 'Post', 'lastName': 'Man'})
USERS.create({'firstName': 'Smart', 'lastName': 'Stub'})





@api.route('/')
class UserList(Resource):
    '''Shows a list of all users, and lets you post new users?'''
    @api.doc('list_users')
    @api.marshal_list_with(user)
    def get(self):
        '''List all users'''
        return USERS.User

    @api.doc('create_user')
    @api.expect(user)
    @api.marshal_with(user, code=201)
    def post(self):
        '''Create a new User'''
        return USERS.create(api.payload), 201


@api.route('/<int:id>')
@api.param('id', 'The users unique identifier')
@api.response(404, 'User not found')
class User(Resource):
    '''Show a single user and can update/delete users'''
    @api.doc('get_user')
    @api.marshal_with(user)
    def get(self, id):
        '''Fetch a user given its identifier'''
        return USERS.get(id)

    @api.doc('delete_user')
    @api.response(204, 'User deleted')
    def delete(self, id):
        '''Delete a user given its identifier'''
        USERS.delete(id)
        return '', 204
        # api.abort(404)