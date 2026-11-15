#!/usr/bin/env python3
"""Provide a simple Flask API for managing users in memory."""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/", methods=["GET"])
def home():
    """Return the API welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_data():
    """Return the list of stored usernames."""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Return the API status."""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return a user or a JSON error if the user does not exist."""
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Validate JSON data and add a new user."""
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not isinstance(username, str) or not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
