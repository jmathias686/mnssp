from flask_restplus import Namespace, Resource, fields, reqparse
import core as dbfn
import json
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
    'vote_id' : fields.Integer(default=-1, description='What movie User has voted on')
})

email = api.model('Email', {'email' : fields.String(required=True, description= 'the user email address')})

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
        #need pass down values
        print(((api.payload['first_name'])))
        insert_str = '\'' + api.payload['first_name'] + '\', \'' + api.payload['last_name'] + '\', \'' + api.payload['email'] +'\', false, 0'
        dbfn.commitDB('insert into users (first_name, last_name, email, attending, vote_id) values ('+ insert_str +')')
        return { 'message' : 'user create success' }, 201


@api.route('/<int:id>')
@api.param('id', 'The users unique identifier')
@api.response(404, 'User not found')
class User(Resource):
    '''Show a single user and can update/delete users'''
    @api.doc('get_user')
    @api.marshal_with(user)
    def get(self, id):
        '''Fetch a user given its identifier'''
        return dbfn.queryDB('select * from users where user_id = ' + id), 200

    @api.doc('delete_user')
    @api.response(204, 'User deleted')
    def delete(self, id):
        '''Delete a user given its identifier'''
        dbfn.commitDB('delete from users where user_id = '+id)
        return {"message": "user " + id + " deleted"}, 204
        # api.abort(404)
    @api.doc('update_user')
    @api.marshal_with(user)
    def put(self,id): #maybe should be patch?
        #add check if exist else return no user
        #need help on what to be updating...? shouldn't need an update
        '''Update user data'''
        #query = 
        #dbfn.commitDB('update users set '+ query +'where user_id = '+id) 
        return {'message':'user ' +id+' updated'}
    



@api.route('/attending')
class Attending(Resource):
    @api.doc('get_list_of_attending_users')
    @api.marshal_list_with(user)
    def get(self):
        '''List all users attending'''
        tuples = dbfn.queryDB('select * from users where attending = true')
        print(tuples)
        return tuples

@api.route('/attending/<int:id>/<string:attend>')
class userAttending(Resource):
    @api.doc('Update attendance of specific user')
    def patch(self, id, attend):
        # usr = USERS.get(id)
        dbfn.commitDB('update users set attending = '+ attend +' where user_id = '+str(id)) 
        return {"message": "attendance updated to "+ attend}, 204

    


@api.route('/emails')
class Emails(Resource):
    @api.doc('get_user_emails')
    @api.marshal_with(email, envelope="Email_list")
    def get(self):
        '''List all user emails'''
        return dbfn.queryDB('select email from users')


@api.route('/emails/<int:id>')
class singleEmail(Resource):
    @api.doc('get_specific_email')
    @api.marshal_with(email)
    def get(self,id):
        '''Show specific user email'''
        return dbfn.queryDB('select email from users where user_id = '+str(id))

