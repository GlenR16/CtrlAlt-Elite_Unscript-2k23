from tensorflow.keras.models import load_model
import keras.utils as image
import numpy as np
from io import BytesIO
classed=['Good', 'Moderate', 'Poor']
model = load_model("./home/assessment/QualityAssess.h5")

def assessment(file):
    # image = BytesIO(file)
    img = image.load_img(file, target_size=(128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)
    return classed[class_idx],prediction[0, class_idx]