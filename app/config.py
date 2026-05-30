import os

# Base directory of the project (cnn_project/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path to trained CNN model
MODEL_PATH = os.path.join(BASE_DIR, "model", "cnn_model.h5")

# Image size for CIFAR-10 dataset
IMG_SIZE = (32, 32)

# CIFAR-10 class labels
CLASS_NAMES = [
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
]