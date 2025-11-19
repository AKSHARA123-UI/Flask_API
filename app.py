from flask import Flask, jsonify, request

app = Flask(__name__)

# Simple API key
API_KEY = "12345"

# In-memory "database" with age and location
users = [
    {"id": 1, "name": "Akshara", "email": "akshara@example.com", "age": 20, "location": "India"},
    {"id": 2, "name": "Vishwa", "email": "vishwa@example.com", "age": 22, "location": "USA"}
]

# Authentication before every request
@app.before_request
def check_api_key():
    key = request.headers.get('x-api-key')
    if key != API_KEY:
        return jsonify({"message": "Unauthorized. Invalid API key."}), 401

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# POST a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"],
        "age": data.get("age", 0),
        "location": data.get("location", "")
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT (update) a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            user["email"] = data.get("email", user["email"])
            user["age"] = data.get("age", user["age"])
            user["location"] = data.get("location", user["location"])
            return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# DELETE a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(i)
            return jsonify({"message": "User deleted"})
    return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
