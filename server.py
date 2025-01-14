"""Este módulo define el servidor Flask para la detección de emociones en un texto dado."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Iniciar la app Flask
app = Flask("Emotion Detector")


@app.route("/emotionDetector", methods=['GET', 'POST'])
def emotion_detector_route():
    """Este endpoint recibe un texto, lo analiza y devuelve las emociones detectadas."""
    text_to_analyze = request.args.get('textToAnalyze')

    # Verificar si el texto está vacío
    if not text_to_analyze:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!", 400

    result = emotion_detector(text_to_analyze)
    dominant_emotion = result['dominant_emotion']

    # Manejar el caso donde la emoción dominante sea None
    if dominant_emotion is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!", 400

    # Respuesta exitosa con resultados de emociones
    output = (f"Para la frase dada, la respuesta del sistema es 'anger': {result['anger']}, "
              f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} y "
              f"'sadness': {result['sadness']}. La emoción dominante es "
              f" {result['dominant_emotion']}.")
    return output, 200


@app.route("/")
def render_index_page():
    """Este endpoint renderiza la página principal de la aplicación."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5008)
