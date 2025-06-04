import numpy as np

def preprocess_image(img, target_size=(256, 256), normalize=True):
    img = img.resize(target_size)
    img_array = np.array(img, dtype=np.float32)
    if normalize:
        img_array = img_array / 255.0
    return np.expand_dims(img_array, axis=0)