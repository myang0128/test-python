from . import auth_api_blueprint
from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
)
from ..models import User

@auth_api_blueprint.route('/login', methods=['POST'])
def login():
    request_json = request.json

    if (
            request_json is None
            or request_json["email"] is None
            or request_json["password"] is None
    ):
        return jsonify({"err_type": "credentials", "err_msg": "empty"}), 400

    email = request.json['email']
    password = request.json['password']

    user = User.query.filter_by(email=email).first()
    if user is None or not password == user.password:
        return jsonify({"msg": "Bad credentials"}), 400

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    ret = {"access_token": access_token, "refresh_token": refresh_token}
    return jsonify(ret), 200