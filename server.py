from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app

app = Flask("Emotion Detector")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
   
    text_to_analyze = request.json.get('text', '')

    result = emotion_detector(text_to_analyze)

    return jsonify(result)


@app.route("/")
def render_index_page():
   
    return render_template('index.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)