from aws_lambda_wsgi import response
from app import app  # Import your Flask app here

def lambda_handler(event, context):
    return response(app, event, context)