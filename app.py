from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model

def load_fingerprint_img(path):
    img_data = img_to_array(load_img(path, color_mode='grayscale', target_size=(97, 90),
                                     interpolation="lanczos", keep_aspect_ratio=True))
    return img_data

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = './uploads'
FINGERPRINT_FOLDER = './samples'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = load_model('./fingerprint_comparison.keras')

print(model.summary())

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    test_img = load_fingerprint_img(filepath)

    max_probability = 0
    identified_person = None

    for person_folder in os.listdir(FINGERPRINT_FOLDER):
        person_path = os.path.join(FINGERPRINT_FOLDER, person_folder)
        
        for finger_folder in os.listdir(person_path):
            finger_path = os.path.join(person_path, finger_folder)
            
            finger_probs = []
            for image_file in os.listdir(finger_path):
                image_path = os.path.join(finger_path, image_file)
                sample_img = load_fingerprint_img(image_path)
                predictions = model.predict((np.array([test_img]), np.array([sample_img])), verbose=0)
                finger_probs.append(predictions[0][0])
            
            if finger_probs:
                max_prob = np.max(finger_probs, axis=0)
                if max_prob > max_probability:
                    max_probability = max_prob
                    identified_person = f"{person_folder}"
    print(max_probability)
    if max_probability >= 0.95:
        message = f"{identified_person} has logged in"
        return jsonify({'message': message}), 200
    else:
        message = "Unauthorized access"
        return jsonify({'message': message}), 200

if __name__ == "__main__":
    app.run(debug=True)  