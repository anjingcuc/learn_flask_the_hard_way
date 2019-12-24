from flask import Blueprint, current_app
from flask_restful import Api

from app.resources.post import PostResource, PostList, PostSchema

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp)

api.add_resource(PostResource, '/posts/<int:post_id>')
api.add_resource(PostList, '/posts')
