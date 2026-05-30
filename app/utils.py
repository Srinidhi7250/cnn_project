import numpy as np
import tensorflow as tf
from PIL import Image
from config import MODEL_PATH, CLASS_NAMES, IMG_SIZE

# Load model once
model = tf.keras.models.load_model(MODEL_PATH)

def preprocess_image(image):
    image = image.resize(IMG_SIZE)
    image = np.array(image) / 255.0

    if image.shape[-1] != 3:
        image = np.stack([image]*3, axis=-1)

    image = np.expand_dims(image, axis=0)
    return image


def predict(image):
    processed = preprocess_image(image)
    predictions = model.predict(processed)

    class_index = np.argmax(predictions)
    confidence = float(np.max(predictions))

    return CLASS_NAMES[class_index], confidence