from flask_restplus import Namespace, Resource, fields, reqparse
import core as dbfn
from flask import jsonify
#NOTE: reqparse will be removed eventually, so a different parser might need to be implemented later
#no authentication right now, just string confirmation
api = Namespace('Users', description='User related operations')


names = api.model('Names', {
    'first_name': fields.String(required=True, description='User first name'),
    'last_name' : fields.String(required=True, description='User last name')
})

user = api.model('User', {
    'user_id': fields.Integer(readonly=True, description='User unique ID'),
    'first_name': fields.String(required=True, description='User first name'),
    'last_name' : fields.String(required=True, description='User last name'),
    'email' : fields.String(required=True, description='User Email address'),
    'attending': fields.Boolean(description='If User attending next event'),
    'vote' : fields.Integer(default=-1, description='What movie User has voted on')
})

email = api.model('Email', {'email' : fields.String(required=True, description= 'the user email address')})


class UserDAO(object):
    def __init__(self):
        self.counter = 0
        self.User = []

    def get(self, id):
        for usr in self.User:
            if usr['id'] == id:
                return usr
        api.abort(404, "User {} doesn't exist".format(id))

    def getAttending(self):
        attendance = []
        for usr in self.User:
            if usr['attending'] == True or usr['attending'] == 'true':
                attendance.append(usr)
        return attendance    

    def create(self, data):
        usr = data
        usr['id'] = self.counter = self.counter + 1
        if 'attending' not in usr:
            usr['attending'] = False
        self.User.append(usr)
        return usr

    # def updateAttending(self, id, attendance):
    #     usr = self.get(id)
    #     usr['attending'] = attendance
    #     return usr

    def update(self, id, data):
        usr = self.get(id)
        usr.update(data)
        return usr

    def delete(self, id):
        usr = self.get(id)
        self.User.remove(usr)

    def getEmails(self):
        email = []
        for usr in self.User:
            if usr['email'] is not None:
                email.append(usr)
        return email

    def getEmailInd(self,id):
        for usr in self.User:
            if usr['id'] == id:
                return usr['user']['email']
        api.abort(404, "User {} doesn't exist".format(id))


USERS = UserDAO()
USERS.create({'first_name': 'External', 'last_name': 'Stub', 'email': 'extstub@gmaill.com'})
USERS.create({'first_name': 'Mule', 'last_name': 'Soft', 'email': 'msoft@gmaill.com', 'attending': True})
USERS.create({'first_name': 'Any', 'last_name': 'Point', 'email': 'anyp@gmaill.com'})
USERS.create({'first_name': 'Post', 'last_name': 'Man', 'email': 'pmpat@gmaill.com'})
USERS.create({'first_name': 'Smart', 'last_name': 'Stub', 'email': 'bigbrain@gmaill.com'})





@api.route('/')
class UserList(Resource):
    '''Shows a list of all users and create new users'''
    @api.doc('list_users')
    @api.marshal_list_with(user, envelope="User_list")
    def get(self):
        '''List all users'''
        tuples = dbfn.queryDB('select * from users')
        return tuples

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
        return {"User {}".format(id) : "deleted"}, 204
        # api.abort(404)

    @api.doc('update_user')
    @api.marshal_with(user)
    def put(self,id):
        '''Update user data'''
        return USERS.update(id, api.payload)
    



@api.route('/attending')
class Attending(Resource):
    @api.doc('get_list_of_attending_users')
    @api.marshal_list_with(user)
    def get(self):
        '''List all users attending'''
        return USERS.getAttending()

    # @api.doc('Update attendance of specific user')
    # @api.marshal_with(user)
    # @api.expect(user)
    # def post(self):
    #     # usr = USERS.get(id)
    #     return USERS.get(id)

    


@api.route('/emails')
class Emails(Resource):
    @api.doc('get_user_emails')
    @api.marshal_with(email, envelope="Email_list")
    def get(self):
        '''List all user emails'''
        return USERS.User


@api.route('/emails/<int:id>')
class singleEmail(Resource):
    @api.doc('get_specific_email')
    @api.marshal_with(email)
    def get(self,id):
        '''Show specific user email'''
        return USERS.get(id)

