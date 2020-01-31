from flask_restplus import Namespace, Resource, fields

api = Namespace('Events', description='Events related operations')


address = api.model('address', {
    'address_1' : fields.String(default='505/525 George St'),
    'address_2' : fields.String(default=''),
    'city' : fields.String(default='Sydney'),
    'state' : fields.String(default='NSW'),
    'postcode' : fields.String(default='2000'),
})

users_attending = api.model('users', {
    'user_id' : fields.Integer(attribute='id',readonly=True)
})

events = api.model('event', {
    'id': fields.String(readonly=True, description='The event identifier'),
    'movie' : fields.String(required=True, description='The movie name'),
    'location' : fields.Nested(address,description='The location of movie'),
    'date' : fields.String(required=True,description='The date of movie'),
    'time' : fields.String(required=True, default='12:00', description='The time of movie'),
    'attendees' : fields.List(fields.Nested(users_attending), description='The list of attendees'),
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
USERS.create({'name' : 'aaa'})
USERS.create({'name' : 'bbb'})
USERS.create({'name' : 'ccc'})
USERS.create({'name' : 'ddd'})
USERS.create({'name' : 'eee'})


EVENTS = UserDAO()
EVENTS.create({'move': 'BadBois4Lyf', 'date': '12/1/17', 'attendees' : USERS.User})





@api.route('/')
class CatList(Resource):
    @api.doc('list_events')
    @api.marshal_list_with(events)
    def get(self):
        '''List all events'''
        return EVENTS.User

@api.route('/<id>')
@api.param('id', 'The Event identifier')
@api.response(404, 'Event not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(events)
    def get(self, id):
        '''Fetch an event given its identifier'''
        for cat in CATS:
            if cat['id'] == id:
                return cat
        api.abort(404)