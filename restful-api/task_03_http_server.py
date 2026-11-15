#!/usr/bin/env python3
"""Serve a simple API using Python's http.server module."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class APIHandler(BaseHTTPRequestHandler):
    """Handle GET requests for the API endpoints."""

    def do_GET(self):
        """Return text or JSON depending on the requested path."""
        status = 200
        content_type = "text/plain"

        if self.path == "/":
            body = "Hello, this is a simple API!"
        elif self.path == "/data":
            content_type = "application/json"
            body = json.dumps({
                "name": "John",
                "age": 30,
                "city": "New York"
            })
        elif self.path == "/status":
            body = "OK"
        elif self.path == "/info":
            content_type = "application/json"
            body = json.dumps({
                "version": "1.0",
                "description": "A simple API built with http.server"
            })
        else:
            status = 404
            body = "Endpoint not found"

        content = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    with HTTPServer(("0.0.0.0", 8000), APIHandler) as server:
        print("Server running at http://localhost:8000")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
