from flask import jsonify

def error_response(message, status=400):
    return jsonify({"error": message}), status

def success_response(message, data=None):
    response = {"message": message}
    if data:
        response["data"] = data
    return jsonify(response)
