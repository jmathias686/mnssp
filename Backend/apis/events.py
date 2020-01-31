from flask_restplus import Namespace, Resource, fields

api = Namespace('Events', description='Cats related operations')


address = api.model('address', {
    'address_1' : fields.String(default='505/525 George St'),
    'address_2' : fields.String(default=''),
    'city' : fields.String(default='Sydney'),
    'state' : fields.String(default='NSW'),
    'postcode' : fields.String(default='2000'),
})


events = api.model('events', {
    'id': fields.String(readonly=True, description='The event identifier'),
    'movie' : fields.String(required=True, description='The movie name'),
    'location' : fields.Nested(address),
    'date' : fields.DateTime(dt_format='rfc822'),
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
        if 'attending' not in usr:
            usr['attending'] = False
        self.User.append(usr)
        return usr

    def update(self, id, data):
        usr = self.get(id)
        usr.update(data)
        return usr

    def delete(self, id):
        usr = self.get(id)
        self.User.remove(usr)





CATS = [
    {'id': 'felix', 'name': 'Felix'},
]





@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(events)
    def get(self):
        '''List all cats'''
        return CATS

@api.route('/<id>')
@api.param('id', 'The cat identifier')
@api.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(events)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        for cat in CATS:
            if cat['id'] == id:
                return cat
        api.abort(404)