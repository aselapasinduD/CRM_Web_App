# Exit on error
set -o errexit

pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Create Super User
py manage.py createsuperuser --no-input || echo "Already have a SuperUser"