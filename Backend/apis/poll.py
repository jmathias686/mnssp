from flask_restplus import Namespace, Resource, fields
import core as dbfn

api = Namespace('Poll', description='User related operations')

movies = api.model('movies', {
    'movie_id': fields.Integer(readonly=True, description='User unique ID'),
    'movieObject': fields.String(required=True, description='Movie Object'),
    'to_show' : fields.Boolean()
})

@api.route('/')
class MovieList(Resource):
    @api.doc('movie_list')
    @api.marshal_list_with(movies)
    def get(self):
        '''List all cats'''
        return dbfn.queryDB('select * from poll')
    #needs working on for payload-------------------------------------------------
    @api.doc('add_movie_poll')
    def post(self):
        jsonObj = api.payload
        dbfn.commitDB('insert into poll (movie_details, to_show) values ('+ jsonObj +', false)')
        return {"message":"movie option added"}

@api.route('/show')
@api.param('boolean')
@api.response(404, 'movie not found')
class showMovie(Resource):
    @api.doc('get_movies')
    @api.marshal_with(movies)
    def get(self, id):
        '''Fetch a movie given its identifier'''
        return dbfn.queryDB('select * from poll where to_show = true')

@api.route('/<id>')
@api.param('id', 'single movie detail')
@api.response(404, 'movie not found')
class Movie(Resource):
    @api.doc('get_movie')
    @api.marshal_with(movies)
    def get(self, id):
        '''Fetch a movie given its identifier'''
        return dbfn.queryDB('select * from poll where movie_id = '+str(id))
    @api.doc('update_movie')
    def patch(self, id):
        '''update a movie to show given an identifier'''
        dbfn.commitDB('update poll set to_show = true where movie_id = '+str(id))
        return {"message":"movie showing"}, 204