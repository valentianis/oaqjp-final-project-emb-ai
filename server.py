''' Executing this function initiates the application of Emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
# Import the emotion_detector function from the package created
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs emotion_detection over it using emotion_detector()
        function. The output returned shows each pair emotion: score
        and the dominant emotion
    '''
    #
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Return a formatted string with each emotion label and its score,
    # indicating the dominant emotion for the Input text
    emo_str = ", ".join(f"'{key}': {value}" for key, value in response.items() if key != 'dominant_emotion')
    resp_str=f"For the given statement {text_to_analyze.upper()}, the system response is {emo_str}. The dominant emotion is {response['dominant_emotion'].upper()}."
    return resp_str



@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
