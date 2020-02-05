from flask_restplus import Namespace, Resource, fields
import core as dbfn
api = Namespace('Events', description='Events related operations')


users_attending = api.model('users', {
    'user_id' : fields.Integer(attribute='id',readonly=True)
})

events = api.model('event', {
    'id': fields.String(readonly=True, description='The event identifier'),
    'movie_title' : fields.String(required=True, description='The movie name'),
    #'movie_detail' : fields.json(something)?
    'date' : fields.String(required=True,description='The date of movie'),
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
    def post(self):
        '''Create a new Event'''
        insert_string = api.payload['date'] + ',' + api.payload['movie_title']
        dbfn.commitDB('insert into events (dates, selected_movie) values (' + insert_string + ')')
        return {"message": "events created"}

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
    def delete(self,id):
        '''deletes a single event given identifier'''
        dbfn.commitDB('delete from events where events_id = '+id)
        return {"message" : "event deleted"}, 204

@api.route('/current')
class Event(Resource):
    @api.doc('get_event')
    @api.marshal_with(events)
    def get(self):
        '''Get current event'''
        #assumption all events are made in order
        return dbfn.queryDB('select * from events order by events_id DESC limit 1')
#TODO -------------------------------------------
@api.route('/current/<int:id>')
class EventAttendee(Resource):
    @api.doc('update_goer')
    def patch(self,id):
        '''modifies movie goer list'''
        curr = dbfn.queryDB('select movie_goers from events order by events_id DESC limit 1')
        # manipulate the movie_goers list and append new id
        # quick call into 'update events set movie_goers = ' + new_list + ' where events_id = max(events_id)'
        dbfn.commitDB('')
        return
