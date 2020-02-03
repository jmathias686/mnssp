from flask_restplus import Namespace, Resource, fields

api = Namespace('Poll', description='User related operations')


user = api.model('user', {
    'user_id': fields.Integer(attribute='id',readonly=True, description='User unique ID'),
    'firstName': fields.String(required=True, description='User first name'),
    'lastName' : fields.String(required=True, description='User last name'),
    'vote_id' : fields.Integer(readonly=True, description='Movie ID') #could change to Id corresponding to movieDB or something?
})

movies = api.model('movies', {
    'movie_id': fields.Integer(readonly=True, description='User unique ID'),
    'movieName': fields.String(required=True, description='Movie Name'),
    'user' : fields.List(fields.Nested(user), description = 'User Votes')
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

    # def getAttending(self):
    #     attendance = []
    #     for usr in self.User:
    #         if usr['attending'] == True:
    #             attendance.append(usr)
    #     return attendance    

    def create(self, data):
        usr = data
        usr['id'] = self.counter = self.counter + 1
        # if 'attending' not in usr:
        #     usr['attending'] = False
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

    # def getEmails(self):
    #     email = []
    #     for usr in self.User:
    #         if usr['email'] is not None:
    #             email.append(usr)
    #     return email

    # #def getEmailInd(self,id):
    #     for usr in self.User:
    #         if usr['id'] == id:
    #             return usr['user']['email']
    #     api.abort(404, "User {} doesn't exist".format(id))


USERS = UserDAO()
USERS.create({'firstName': 'External', 'lastName': 'Stub', 'vote_id' : 1})
USERS.create({'firstName': 'Mule', 'lastName': 'Soft','vote_id' : 1})
USERS.create({'firstName': 'Any', 'lastName': 'Point', 'vote_id': 2})
USERS.create({'firstName': 'Post', 'lastName': 'Man', 'vote_id' : 2})
USERS.create({'firstName': 'Smart', 'lastName': 'Stub',  'vote_id' : 1})



class MoviesDAO(object):
    def __init__(self):
        self.counter =0
        self.Movies = []

    def get(self, id):
        for mvs in self.Movies:
            if Movies['id'] == id:
                return mvs
        api.abort(404, "Movie {} doesn't exist".format(id))

    def create(self, data):
        mvs = data
        mvs['id'] = self.counter = self.counter + 1
        #mvs['user'] = USERS.User
        # if 'attending' not in usr:
        #     usr['attending'] = False
        self.Movies.append(mvs)
        return mvs

    def delete(self, id):
        mvs = self.get(id)
        self.Movies.remove(mvs)




MOVIES = MoviesDAO()
MOVIES.create({'movie_id': 1, 'movieName': 'Bad Boys for life', 'User': '' })
MOVIES.create({'movie_id': 2, 'movieName': '1917', 'User': ''})

#MOVIES = MoviesDAO()



@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(movies)
    def get(self):
        '''List all cats'''
        return MOVIES.Movies

@api.route('/<id>')
@api.param('id', 'The cat identifier')
@api.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(movies)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        for cat in CATS:
            if cat['id'] == id:
                return cat
        api.abort(404)