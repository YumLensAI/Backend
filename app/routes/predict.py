from flask import Blueprint, request, jsonify
from PIL import Image

from app.config import MODEL_PATH, MODEL_WEIGHTS
from app.services.inference import load_tflite_model, run_inference, get_class_and_confidence
from app.services.image import preprocess_image

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file in the request'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        img = Image.open(file.stream)
        interpreter = load_tflite_model(MODEL_PATH)
        image_array = preprocess_image(img)
        classes = run_inference(interpreter, image_array)
        resultado = get_class_and_confidence(classes.flatten())
        unique_fruits = list(set(MODEL_WEIGHTS[item['classId']] for item in resultado))

        return jsonify(unique_fruits)
    except Exception as e:
        return jsonify({'error': str(e)}), 500