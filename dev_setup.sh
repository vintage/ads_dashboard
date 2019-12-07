virtualenv .venv -p python3
source .venv/bin/activate
pip install -r requirements.txt
cd ads_dashboard
./manage.py migrate
./manage.py load_stats
./manage.py runserver
