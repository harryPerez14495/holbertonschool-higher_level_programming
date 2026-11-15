#!/usr/bin/env python3
"""Protect a Flask API with Basic authentication, JWT, and roles."""

import os
import secrets
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt,
    jwt_required
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = (
    os.environ.get("JWT_SECRET_KEY") or secrets.token_hex(32)
)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Return the username if the supplied credentials are valid."""
    if not isinstance(username, str) or not isinstance(password, str):
        return None
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@auth.error_handler
def basic_auth_error(status):
    """Return 401 when Basic authentication fails."""
    return jsonify({"error": "Unauthorized"}), 401


@jwt.unauthorized_loader
def missing_token(reason):
    """Return 401 when a JWT is missing."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token(reason):
    """Return 401 when a JWT is invalid or malformed."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token(header, payload):
    """Return 401 when a JWT has expired."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token(header, payload):
    """Return 401 when a JWT has been revoked."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def fresh_token_required(header, payload):
    """Return 401 when a fresh JWT is required."""
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Return a message after successful Basic authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Validate credentials and issue a JWT containing the user's role."""
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid credentials"}), 401

    username = data.get("username")
    password = data.get("password")
    if verify_password(username, password) is None:
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )
    return jsonify({"access_token": token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Return a message after successful JWT authentication."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Allow access only when the JWT contains the admin role."""
    if get_jwt().get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
