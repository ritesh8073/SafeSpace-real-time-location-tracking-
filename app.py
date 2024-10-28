from flask import Flask, send_from_directory
from routes import api_routes

app = Flask(__name__, static_folder='../client', static_url_path='')

# Register API routes
app.register_blueprint(api_routes)

@app.route('/')
def index():
    return send_from_directory('../client', 'index.html')

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('../client', path)

if __name__ == '__main__':
    app.run(debug=True)
