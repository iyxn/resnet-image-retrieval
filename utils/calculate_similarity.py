from utils.feature_extractor import FeatureExtractor
from PIL import Image
import numpy as np
import glob

feature_path = "features/features_resnet50.npy"
fe = FeatureExtractor()
def dataset():
    img_paths = glob.glob("data/*")
    return img_paths
def upload_images(img):
    img = Image.open(img)
    query = fe.extract(img)
    scores = similarity(query)
    return scores

def similarity(query):
    features = np.load(feature_path)
    distance = np.linalg.norm(features - query, axis=1)
    ids = np.argsort(distance)[:30]
    img_paths = dataset()
    scores = [(distance[id], img_paths[id]) for id in ids]
    return scores