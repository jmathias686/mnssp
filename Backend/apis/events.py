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
    'no_attend' : fields.Integer(required=True, description='The number of attendees'),
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






class EventsDAO(object):
    def __init__(self):
        self.counter = 0
        self.Event = []

    def get(self, id):
        for ind in self.Event:
            if ind['id'] == id:
                return ind
        api.abort(404, "Event {} doesn't exist".format(id))

    def create(self, data):
        ind = data
        ind['id'] = self.counter = self.counter + 1
        ind['no_attend'] = len(USERS.User)
        ind['attendees'] = USERS.User
        self.Event.append(ind)
        return ind

    def update(self, id, data):
        ind = self.get(id)
        ind.update(data)
        return ind

    def delete(self, id):
        ind = self.get(id)
        self.Event.remove(ind)


EVENTS = EventsDAO()
EVENTS.create({'movie': 'BadBois4Lyf', 'date': '12/1/17'})





@api.route('/')
class EventList(Resource):
    @api.doc('list_events')
    @api.marshal_list_with(events)
    def get(self):
        '''List all events'''
        return EVENTS.Event

    @api.doc('create_event')
    @api.expect(events)
    @api.marshal_with(events, code=201)
    def post(self):
        '''Create a new Event'''
        return EVENTS.create(api.payload), 201


@api.route('/current')
class Event(Resource):
    @api.doc('get_event')
    @api.marshal_with(events)
    def get(self):
        '''Get current event'''
        id = EVENTS.counter
        return EVENTS.get(id)


@api.route('/<int:id>')
@api.param('id', 'The Event identifier')
@api.response(404, 'Event not found')
class EventSpecific(Resource):
    @api.doc('get_specific_event')
    @api.marshal_with(events)
    def get(self, id):
        '''Get specific event given identifier - for past events'''
        return EVENTS.get(id)
        # api.abort(404)