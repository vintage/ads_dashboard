# ads_dashboard

![Preview](preview.png?raw=true "Preview")

## Local setup

1. Enter the main directory
2. Create new virtualenv based on Py3 `virtualenv .venv -p python3` (or any other tool for managing virtual envs in Python)
3. Activate virtualenv `source .venv/bin/active`
4. Install requried dependencies `pip install -r requirements.txt`
5. Enter Django directory `cd ads_dashboard`
6. Sync the database `python manage.py migrate`
7. Load initial data `python manage.py load_stats`
8. Start server `python manage.py runserver`
9. Application is now accesible at `http://localhost:8000/`

Or simply:
1. Run `./dev_setup.sh`
2. Point browser to `http://localhost:8000/`

## Not implemented

1. Tests (not even single one)
2. Docker setup through docker-compose
3. Separation of backend (Django, GraphQL) and frontend (React, Apollo)
4. Keeping the secrets secret (env variables)
5. Many other
