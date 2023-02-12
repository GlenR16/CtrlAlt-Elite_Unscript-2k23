from tensorflow.keras.models import load_model
import keras.utils as image
import numpy as np
from io import BytesIO
classed=['Good', 'Moderate', 'Poor']
model = load_model("./home/assessment/QualityAssess.h5")

def assessment(file):
    # image = BytesIO(file)
    img = image.load_img(file.file, target_size=(128, 128))
    # Convert the image to a Numpy array
    img_array = image.img_to_array(img)
    # Add an extra dimension to the array to make it suitable for input to the model
    img_array = np.expand_dims(img_array, axis=0)
    # Make a prediction on the image
    prediction = model.predict(img_array)
    # Get the class with the highest predicted probability
    class_idx = np.argmax(prediction)
    # Print the prediction
    return classed[class_idx],prediction[0, class_idx]