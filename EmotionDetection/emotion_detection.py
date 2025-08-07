# Import the requests library to handle HTTP requests
import requests
import json

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):  
    # URL of emotion predit service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers = header)

    # If the response status code is 200, extract the relevant information from the response
    if response.status_code == 200:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)

        # Extracting emotional scores from the response
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    
        #finding the dominant emotion by comparing scores
        dominant_emotion = 'NONE'
        dominant_emotion_score = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)

        if dominant_emotion_score == anger_score:
            dominant_emotion = 'ANGER'
        elif dominant_emotion_score == disgust_score:
            dominant_emotion = 'DISGUST'
        elif dominant_emotion_score == fear_score:
            dominant_emotion = 'FEAR'
        elif dominant_emotion_score == joy_score:
            dominant_emotion = 'JOY'
        else:
            dominant_emotion = 'SADNESS'    

    # If the response status code is 400, set values to None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    # Returning a dictionary containing emotion predict results
    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score,
    'dominant_emotion': dominant_emotion}