# Import the libraries
from tensorflow.keras.preprocessing import image # type: ignore
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input # type: ignore
from tensorflow.keras.models import Model # type: ignore
import numpy as np

class FeatureExtractor:
    def __init__(self):
        base_model = ResNet50(weights='imagenet', input_shape=(224, 224, 3), include_top=False, pooling='avg')
        self.model = Model(inputs=base_model.input, outputs=base_model.output)

    def extract(self, img):
        img = img.resize((224, 224))
        img = img.convert('RGB')
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        feature = self.model.predict(x)[0]
        
        return feature / np.linalg.norm(feature)