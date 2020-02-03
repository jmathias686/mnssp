from flask_restplus import Namespace, Resource, fields
import core as dbfn
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

@api.route('/')
class EventList(Resource):
    @api.doc('list_events')
    @api.marshal_list_with(events)
    def get(self):
        '''List all events'''
        return dbfn.queryDB('select * from events'), 200

    @api.doc('create_event')
    @api.expect(events)
    @api.marshal_with(events, code=201)
    def post(self):
        '''Create a new Event'''
        insert_string = dates + ',' + selected_movie
        dbfn.commitDB('insert into events (dates, selected_movie) values (' + insert_string + ')')
        return {"message": "events created"}

@api.route('/current')
class Event(Resource):
    @api.doc('get_event')
    @api.marshal_with(events)
    def get(self):
        '''Get current event'''
        #assumption all events are made in order
        return dbfn.queryDB('select * from events order by events_id DESC limit 1')

@api.route('/current/attendee/<int:id>')
class EventAttendee(Resource):
    @api.doc('update_goer')
    def patch(self,id):
        curr = dbfn.queryDB('select movie_goers from events order by events_id DESC limit 1')
        #manipulate the movie_goers list and append new id
        #quick call into 'update events set movie_goers = ' + new_list + ' where events_id = max(events_id)'
        dbfn.commitDB('')
        return

@api.route('/current/dining/<int:id>')
class EventDining(Resource):
    @api.doc('update_diner')
    def patch(self,id):
        curr = dbfn.queryDB('select dining_goers from events order by events_id DESC limit 1')
        # manipulate the dining_goers list and append new id
        # quick call into 'update events set movie_goers = ' + new_list + ' where events_id = max(events_id)'
        
        dbfn.commitDB('')
        return

@api.route('/<int:id>')
@api.param('id', 'The Event identifier')
@api.response(404, 'Event not found')
class EventSpecific(Resource):
    @api.doc('get_specific_event')
    @api.marshal_with(events)
    def get(self, id):
        '''Get specific event given identifier - for past events'''
        return dbfn.queryDB('select * from events where events_id = '+str(id))
        # api.abort(404)