
- Python virtual environment
```python
python3.10 -m venv .venv
source /Users/shrutisinha/REST-APIs-with-Python/.venv/bin/activate
pip install -r requirements.txt
deactivate
```
- To initialize database migration with Flask-Migrate
```python
flask db init
# delete data.db
flask db migrate
flask db upgrade
```
- Generate database migration with changes to SQLAlchemy models
```python
flask db migrate
# This will now generate another migration script that you have to double-check. Make sure to check the upgrade and downgrade functions.
# When you're happy with the contents, apply the migration.
flask db upgrade
```
- Build Docker image into a new container and run container with automatic reloading
```python
docker build -t rest-apis-with-flask-python .
docker run -dp 5005:5000 -w /app -v "$(pwd):/app" rest-apis-with-flask-python
docker rm CONTAINER_ID
```