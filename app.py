from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Inicializar la aplicación Flask
app = Flask(__name__)

# Cargar el modelo entrenado
model = tf.keras.models.load_model('image_recognition_model.h5')

# Rutas de la aplicación
@app.route('/predict', methods=['POST'])
def predict():
    # Leer la imagen de la solicitud
    file = request.files['file']
    img = Image.open(io.BytesIO(file.read())).resize((32, 32))
    
    # Preprocesar la imagen
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Realizar la predicción
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction[0])

    return jsonify({'prediction': int(predicted_class)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
