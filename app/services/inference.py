import tensorflow as tf

def load_tflite_model(model_path):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

def run_inference(interpreter, image_array):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(input_details[0]['index'], image_array)
    interpreter.invoke()

    classes = interpreter.get_tensor(output_details[1]['index'])[0]
    return classes

def get_class_and_confidence(scores, num_classes=7, threshold=0.5):
    results = []
    for i in range(0, len(scores), num_classes):
        class_scores = scores[i:i + num_classes]
        confidence = max(class_scores)
        class_id = class_scores.tolist().index(confidence)
        if confidence > threshold:
            results.append({'classId': class_id, 'confidence': float(round(confidence, 2))})
    return results