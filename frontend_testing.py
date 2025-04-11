from flask import Flask, request, jsonify

app = Flask(__name__)

users_db = {}

def error_return(reason, error_code):
    return jsonify({"status": "error", "reason": f"{reason}"}), error_code


@app.route('/users/<int:user_id>', methods=['POST'])
def add_user(user_id):
    data = request.get_json() #extract json data from the post request

    if not data:
        #if no json data is sent - return error
        return error_return("no JSON data provided", 400)

    if 'user_name' not in data:
        return error_return("Missing user_name", 400)

    user_name = data['user_name']

    if not user_name.strip():
        return error_return("user_name cannot be empty"), 400

    if user_id in users_db:
        error_return("ID already exists", 500)

    users_db[user_id] = user_name

    return jsonify({"status": "ok", "user_added": user_name}), 200

if __name__ == '__main__':
    app.run(debug=True)