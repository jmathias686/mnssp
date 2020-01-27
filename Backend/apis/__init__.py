from flask_restplus import Api
from .user import api as user_api
from .events import api as events_api

api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(user_api)
api.add_namespace(events_api)