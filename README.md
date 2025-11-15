# ORION_unleashed

ORION Unleashed is a Flask-based web application with IPFS and GitHub integration.

## Deployment Instructions

### 1. Entpacken (Extract)
```bash
cd ORION_DEPLOY_PACKAGE/
```

### 2. Abhängigkeiten installieren (Install Dependencies)
```bash
pip install -r requirements.txt
```

### 3. Konfiguration (Configuration)
```bash
cp .env.example .env
```
➤ Edit `.env` and configure:
- `API_KEY`: Your API key
- `IPFS_HOST`: IPFS host (default: localhost)
- `IPFS_PORT`: IPFS port (default: 5001)
- `GITHUB_TOKEN`: Your GitHub personal access token

### 4. Starten (Start)
```bash
gunicorn --bind 0.0.0.0:5000 main:app
```

## Development

To run in development mode:
```bash
python main.py
```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check with configuration status
- `GET /config` - Configuration information (without sensitive data)