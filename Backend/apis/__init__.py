from flask_restplus import Api

from .user import api as user_api
from .events import api as events_api
from .poll import api as poll_api

api = Api(
    title='MNSSP Platform',
    version='1.0',
    description='Movie Night Self Service Protocol (MNSSP) is a Platform to streamline the process of organising a movie night for DPE',
    # All API metadatas
)

api.add_namespace(user_api)
api.add_namespace(events_api)
api.add_namespace(poll_api)

