import requests # Import the requests library to handle HTTP requests
import os
import  json
from dotenv import load_dotenv # Load environment variables from a .env file
from requests.auth import HTTPBasicAuth

# Load environment variables
load_dotenv()

# Retrieve the API key and URL from environment variables
API_KEY = os.getenv("WATSON_API_KEY")
API_URL = os.getenv("WATSON_API_URL")

def sentiment_analyzer(text_to_analyse):
    """Function to analyze sentiment using the Watson NLP service."""

    # Check if API_KEY and API_URL are correctly loaded
    if not API_KEY or not API_URL:
        raise ValueError("API key or URL is not set in the environment variables.")
    
    url = f"{API_URL}/v1/analyze"  # URL of the sentiment analysis service
    
    # Prepare the input JSON payload
    params = {
        "version": "2021-08-01",  # Specify the API version
        "features": {"sentiment": {}},  # Use the sentiment analysis feature
        "text": text_to_analyse   # The text to be analyzed
    }

    # Set up the headers (Authorization with Basic Auth using the API key)
    headers = {"Content-Type": "application/json"}
    
    # Use Basic Authentication for Watson API using the API key
    response = requests.post(url, json=params, headers=headers, auth=HTTPBasicAuth('apikey', API_KEY))
    
    # Raise an exception if the response contains an error
    response.raise_for_status()
    
     # Parse the response JSON text into a dictionary
    formatted_response = json.loads(response.text)
    
    # Extract the label and score from the nested dictionary
    label = formatted_response['sentiment']['document']['label']
    score = formatted_response['sentiment']['document']['score']

    
    # Return the extracted values as a dictionary
    return {'label': label, 'score': score}
