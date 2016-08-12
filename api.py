from flask import Flask
from flask_httpauth import HTTPTokenAuth
from flask_restful import Resource, Api, fields, marshal_with, abort

from models import Item


app = Flask(__name__)
api = Api(app)
auth = HTTPTokenAuth(scheme='Token')


valid_tokens = {'token1', 'token2'}


@auth.verify_token
def verify_token(token):
    return token in valid_tokens


inventory_fields = dict(
    id=fields.Integer,
    name=fields.String,
    description=fields.String,
    price=fields.Integer
)


class ItemList(Resource):
    @marshal_with(inventory_fields)
    def get(self):
        return Item.get_all().values()


class ItemPurchaseSimple(Resource):
    @auth.login_required
    def post(self, id):
        try:
            item = Item.get(id)
        except KeyError:
            abort(404, message='Item does not exist')

        return {'success': item.purchase()}


api.add_resource(ItemList, '/items')
api.add_resource(ItemPurchaseSimple, '/items/<int:id>/purchase')

if __name__ == '__main__':
    app.run(debug=True)