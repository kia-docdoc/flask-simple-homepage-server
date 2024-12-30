from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static')

# Replace these placeholders with your actual subdomains and corresponding information
subdomains = [
    {"name": "Media Center", "description": "Films", "url": "https://v6media.babadoc.online"},
    {"name": "Bibliotheca", "description": "Books", "url": "https://library.babadoc.online"},
    {"name": "Download Server", "description": "Hosted files", "url": "https://v6downloads.babadoc.online"},
    {"name": "AI Chat", "description": "Yoongi", "url": "https://chat.babadoc.online"},
    #{"name": "Server Monitor", "description": "Live status", "url": "https://monitor.babadoc.online"},
]

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html', subdomains=subdomains)

if __name__ == '__main__':
    app.run(debug=True, port=2052, host='::')
