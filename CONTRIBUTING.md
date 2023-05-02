
- Python virtual environment
```python
python3.10 -m venv .venv
source /Users/shrutisinha/REST-APIs-with-Python/.venv/bin/activate
pip install -r requirements.txt
deactivate
```

- Build Docker image into a new container and run container with automatic reloading
```python
docker build -t rest-apis-with-flask-python .
docker run -dp 5005:5000 -w /app -v "$(pwd):/app" rest-apis-with-flask-python
docker rm CONTAINER_ID
```