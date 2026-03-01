import pickle
import numpy as np
import os

# get correct paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")
VEC_PATH = os.path.join(BASE_DIR, "model", "vectorizer.pkl")

# load model
model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VEC_PATH, "rb"))

SCAM_WORDS = [
    "earn money",
    "work from home",
    "no experience",
    "registration fee",
    "payment required"
]

def predict_job(text):
    # vectorize
    vec = vectorizer.transform([text])

    # scam flag feature
    scam_flag = int(any(word in text.lower() for word in SCAM_WORDS))

    # combine features (same as training)
    combined = np.hstack([vec.toarray(), [[scam_flag]]])

    pred = model.predict(combined)[0]
    prob = model.predict_proba(combined)[0][1]

    return {
        "prediction": "Fake" if pred == 1 else "Legit",
        "confidence": float(prob)
    }