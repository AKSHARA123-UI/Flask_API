## Code Description

This Flask application is a simple REST API to manage user data. 

Features:
- **GET /users**: Retrieve a list of all users.
- **GET /users/<id>**: Retrieve details of a single user by ID.
- **POST /users**: Add a new user by providing JSON data (name, email, age, location).
- **PUT /users/<id>**: Update existing user details by ID using JSON data.
- **DELETE /users/<id>**: Delete a user by ID.
- **API Key Authentication**: All requests require a valid `x-api-key` in headers.
- **In-memory Storage**: User data is stored in a Python list (resets on server restart).

Tools Used:
- Python 3.x
- Flask
- Postman or curl for testing

How to Run:
1. Clone or download the project.
2. Create and activate a virtual environment.
3. Install dependencies: `pip install flask`
4. Run the server: `python app.py`
5. Use Postman or curl to interact with the API endpoints.
