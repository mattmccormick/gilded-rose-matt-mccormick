from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with
from models import Item

app = Flask(__name__)
api = Api(app)


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


class ItemSimple(Resource):
    def post(self, id):
        pass


api.add_resource(ItemList, '/items')
api.add_resource(ItemSimple, '/item/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)