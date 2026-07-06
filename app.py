from flask import Flask, render_template, request, redirect, jsonify, abort
import json
import os
import string
import random

app = Flask(__name__)
DATA_FILE = 'links.json'

# Helper function: Read from JSON
def load_links():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

# Helper function: Write to JSON
def save_links(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Helper function: Generate 6-char code
def generate_short_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form.get('url', '').strip()
    
    # Validation: Must not be empty and must start with http:// or https:// [cite: 429]
    if not original_url or not original_url.startswith(('http://', 'https://')):
        error_msg = "Invalid URL! Must start with http:// or https://"
        return render_template('index.html', error=error_msg)
    
    links = load_links()
    short_code = generate_short_code()
    
    # Ensure code is unique
    while short_code in links:
        short_code = generate_short_code()
        
    # Save to dictionary and write to JSON [cite: 424]
    links[short_code] = {
        'original_url': original_url,
        'clicks': 0
    }
    save_links(links)
    
    short_url = request.host_url + 's/' + short_code
    return render_template('index.html', short_url=short_url)

@app.route('/s/<code>')
def redirect_link(code):
    links = load_links()
    
    # Return 404 if code doesn't exist [cite: 426]
    if code not in links:
        abort(404, description="Short link not found.")
        
    # Increment click counter and save back to JSON [cite: 428, 469-470]
    links[code]['clicks'] += 1
    save_links(links)
    
    return redirect(links[code]['original_url'])

@app.route('/dashboard')
def dashboard():
    links = load_links()
    return render_template('dashboard.html', links=links)

@app.route('/api/links')
def api_links():
    links = load_links()
    return jsonify(links)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)