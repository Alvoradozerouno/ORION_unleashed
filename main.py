"""
ORION Unleashed - Main Application
"""
import os
from flask import Flask, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Flask application
app = Flask(__name__)

# Configuration from environment variables
app.config['API_KEY'] = os.getenv('API_KEY', '')
app.config['IPFS_HOST'] = os.getenv('IPFS_HOST', 'localhost')
app.config['IPFS_PORT'] = os.getenv('IPFS_PORT', '5001')
app.config['GITHUB_TOKEN'] = os.getenv('GITHUB_TOKEN', '')


@app.route('/')
def index():
    """Root endpoint"""
    return jsonify({
        'message': 'Welcome to ORION Unleashed',
        'status': 'running',
        'version': '1.0.0'
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'api_configured': bool(app.config['API_KEY']),
        'ipfs_configured': bool(app.config['IPFS_HOST']),
        'github_configured': bool(app.config['GITHUB_TOKEN'])
    })


@app.route('/config')
def config():
    """Configuration status endpoint (without sensitive data)"""
    return jsonify({
        'ipfs_host': app.config['IPFS_HOST'],
        'ipfs_port': app.config['IPFS_PORT'],
        'api_key_set': bool(app.config['API_KEY']),
        'github_token_set': bool(app.config['GITHUB_TOKEN'])
    })


if __name__ == '__main__':
    # Development server
    # Debug mode should be controlled via environment variable for security
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
