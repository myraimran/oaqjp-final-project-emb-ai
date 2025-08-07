''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotional scores
        and the dominant emotion for the provided text.
    '''

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the relevant information from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if the label is None, indicating an error or invalid input
    if anger_score is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with the emotional scores and dominant emotion
    message_1 = f"'anger': {anger_score}, 'disgust': {disgust_score},"
    message_2 = f" 'fear': {fear_score}, 'joy': {joy_score}, 'sadness': {sadness_score}"
    scores = f"{message_1}{message_2}"
    return f"The emotional scores are {scores}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
