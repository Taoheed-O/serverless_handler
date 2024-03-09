import awsgi
from app import app # Importing your Flask app

def lambda_handler(event, context):
   return awsgi.response(app, event, context)