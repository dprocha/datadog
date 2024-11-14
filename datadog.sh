ENV_DIR=".venv"
export DD_SITE=us5.datadoghq.com
export DD_API_KEY=696dd587e120faa9521069a499240bff 
export DD_APP_KEY=f4d6556ddf9e50de7eb54bb62cb97f123ee1bdac

source "$ENV_DIR/bin/activate"

python3 "datadog.py"