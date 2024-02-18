# Exit on error
set -o errexit

pip install -r requirements.txt

# Convert static asset files
python ./dcrm/manage.py collectstatic --no-input

# Apply any outstanding database migrations
python ./dcrm/manage.py migrate