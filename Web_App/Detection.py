from flask import Flask, render_template, request
import os
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array, smart_resize


# Initialize Flask app
app = Flask(__name__)

# Load your trained model
model = tf.keras.models.load_model('best_model.h5')

# Define function to process the uploaded image
def process_image(image_path):
    

    img = load_img(image_path, color_mode='grayscale')
    img_array = img_to_array(img)

    img_array_resized = smart_resize(img_array, (512, 512)) # resize the image to 512 by 512
    img_array_reshaped = np.reshape(img_array_resized, (512, 512)) # reshape the image from (512, 512, 1) to (512, 512)

    img_array = img_array_reshaped / 255.0
    return img_array


def preprocess_image(image_path):
    img = Image.open(image_path).convert('L')  # Convert image to grayscale
    img = img.resize((512, 512))  # Resize image to match input size of the model
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Define a route to handle image uploads
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():



    image = request.files['image']
    file_path = 'Image/uploaded_image.jpg'
    image.save(file_path)



    img_array = preprocess_image(file_path)

    # Make prediction
    prediction = model.predict(img_array)
    pred = np.argmax(prediction, axis=1) #pick class with highest  probability
    print("========================================================================", pred)

    if pred == 0:
        result = 'Malignant'
    elif pred == 1:
        result = 'Bengin'

    image_path = '../Image/uploaded_image.jpg'
    d = {'file': image_path, 'output': result}

    
    return render_template('Upload.html', show=True, d = d)

   

# Define a route to handle homepage
@app.route('/')
def home():
    return render_template('Upload.html', show=False)

if __name__ == '__main__':
    app.run(debug=True)

























