import os

# Directory where downloads will be saved
DOWNLOAD_DIR = os.environ.get('DOWNLOAD_DIR', '/tmp/downloads')
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# List of supported platforms
SUPPORTED_PLATFORMS = [
    'classplus', 'studyiq', 'pw', 'khangs', 'careerwill', 'vision', 'allen'
]

# Example for API credentials (set these in your Render environment variables)
API_ID = os.environ.get('27433400')
API_HASH = os.environ.get('1a286620de5ffe0a7d9b57e604293555')
BOT_TOKEN = os.environ.get('8457218709:AAGZpkE5j2YYE0FzoIXxe7d97qSTXcWwVyY')
