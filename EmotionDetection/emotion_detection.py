import requests # Import the requests library to handle HTTP requests
import json # Import the requests library to handle JSON 

def emotion_detector (text_to_analyse): # Define a function named emotion_detector that takes a string
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion predict service
    myobj = { "raw_document": { "text": text_to_analyse } } # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers 
    
    if response.status_code == 400:
        # Initalize dummy output
        emotion_output= {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:
        # Parsing the JSON response from the API 
        json_resp= json.loads(response.text)
        
        # Extracting the required set of emotions, including anger, disgust, fear, joy and sadness, along with their scores.
        emotion_output= json_resp['emotionPredictions'][0]['emotion']

        # Determining the name of the dominant emotion (with max score).
        label_maxscore = max(emotion_output, key= emotion_output.get) 

        # Adding the key dominant_emotion to the output
        emotion_output['dominant_emotion'] = label_maxscore

    # Returning a dictionary containing results 
    #emotion_output= {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    return emotion_output