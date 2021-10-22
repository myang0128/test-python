from flask_jwt_extended import jwt_required

from . import order_api_blueprint
from .. import db
from flask import jsonify, request, make_response
from ..models import Order


@order_api_blueprint.route('/api/orders', methods=['GET'])
@jwt_required()
def orders():
    items = []
    for row in Order.query.all():
        items.append(row.to_json())

    return jsonify(items), 200
