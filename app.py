# app.py
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello_world():
    """
    This function is called when a user accesses the root URL.
    It returns a simple "Hello, World from Flask!" message.
    """
    return 'Hello, World from Flask in Kubernetes via Argo CD!'

# Define a health check endpoint
@app.route('/health')
def health_check():
    """
    A simple health check endpoint that returns "OK".
    Useful for Kubernetes liveness and readiness probes.
    """
    return 'OK', 200

# Run the Flask development server
if __name__ == '__main__':
    # Make the server publicly available (within the container)
    # Listen on port 5000
    app.run(host='0.0.0.0', port=5000)
