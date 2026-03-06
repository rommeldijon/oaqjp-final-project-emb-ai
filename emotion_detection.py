import requests # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse): # Define a function named emotion_detector
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document":{ "text": text_to_analyse}} # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}# Set the headers required for the API request
    response = requests.post(url, json=myobj, headers=header)

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting sentiment label and score from the response
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']
    
    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}