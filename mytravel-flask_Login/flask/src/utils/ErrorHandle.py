from flask import make_response, jsonify


def bad_request(message):
    return make_response(jsonify({"message": message}), 400)


def not_found(message):
    return make_response(jsonify({"message": message}), 404)
