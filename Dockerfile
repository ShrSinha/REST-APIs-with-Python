# To run api in docker with automatic reloading
# docker run -dp 5005:5000 -w /app -v "$(pwd):/app" rest-apis-with-flask-python
FROM python:3.11
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "flask", "run", "--host", "0.0.0.0" ]