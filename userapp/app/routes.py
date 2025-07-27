from flask import request
from .utils import error_response, success_response

users = {}

def register_routes(app):
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        if not data or 'username' not in data:
            return error_response("Missing 'username' field.")

        username = data['username']
        users[username] = data

        if app.redis:
            app.redis.set(username, str(data))

        return success_response(f"User '{username}' registered successfully.", data)

    @app.route('/user/<username>', methods=['GET'])
    def get_user(username):
        if app.redis:
            cached = app.redis.get(username)
            if cached:
                return success_response(f"User '{username}' found in cache.", eval(cached))

        user = users.get(username)
        if user:
            return success_response(f"User '{username}' retrieved from memory.", user)

        return error_response("User not found.", 404)
