from flask_restplus import Namespace, Resource, fields
import requests
import core as dbfn
from .tmdb import tmdb
import json

api = Namespace('Poll', description='User related operations')


movies = api.model('movies', {
    'title': fields.String(required=True, description='Title'),
    'overview' : fields.String(required=True, description='Overview'),
    'popularity' : fields.Integer(description='tmdb Popularity'), #could change to Id corresponding to movieDB or something?
    'vote_average' : fields.Integer(description='tmdb Vote Average'),
    'vote_count' : fields.Integer(description='tmdb Vote Count')
})

poll = api.model('poll', {
    'movie_id': fields.Integer(readonly=True, description='Movies unique ID'),
    'movie_title': fields.String(required = True, description='Movie Title for easy access'),
    'movie_details' : fields.Nested(movies, required = True, description = 'Movie Details'),
    'votes' : fields.Integer( description='The list of votes'),
    'to_show' : fields.Boolean(default = False)

})
votes = api.model('votes',{
    'votes' : fields.Integer(readonly=True, description=' movie\'s vote ID')
})




@api.route('/')
class MovieList(Resource):
    @api.doc('movie_list')
    @api.marshal_list_with(poll)
    def get(self):
        '''List all options'''
        return dbfn.queryDB('select * from poll')
    #needs working on for payload-------------------------------------------------
    @api.doc('add_movie_options')
    @api.expect(poll)
    def post(self):
        #change to requests
        # res = tmdb(self)
        # print(res)
        jsonObj = api.payload
        dbfn.commitDB('insert into poll (movie_details, to_show) values ('+ jsonObj +', false)')
        return {"message":"movie option added"}

@api.route('/show')
@api.response(404, 'movie not found')
class showMovie(Resource):
    @api.doc('get_movies')
    @api.marshal_with(poll)
    def get(self):
        '''Fetch a movie given required to show '''
        return dbfn.queryDB('select * from poll where to_show = True')

@api.route('/<id>')
@api.param('id', 'single movie detail')
@api.response(404, 'movie not found')
class Movie(Resource):
    @api.doc('get_movie')
    @api.marshal_with(poll)
    def get(self, id):
        '''Fetch a movie given its identifier'''
        return dbfn.queryDB('select * from poll where movie_id = '+str(id))
    @api.doc('update_movie')
    def patch(self, id):
        '''update a movie to show given an identifier'''
        dbfn.commitDB('update poll set to_show = true where movie_id = '+str(id))
        return {"message":"movie showing"}, 204

@api.route('/count')
class MovieList(Resource):
    @api.doc('vote_list')
    @api.marshal_list_with(votes)
    def get(self):
        '''List all options'''
        return dbfn.queryDB('select votes from poll')

@api.route('/count/<int:id>')
class MovieList(Resource):
    @api.doc('vote_add')
    def post(self,id):
        #by contract, assign the user with vote id on client side
        #id is movie id
        count = dbfn.queryDB('select votes from poll where movie_id = '+str(id))
        
        dbfn.commitDB('update poll set id = ' + str() + 'where movie_id = '+str(id))
        return {"message" : "updated count"}