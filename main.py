import streamlit as st
import numpy as np
import cv2
import joblib
from PIL import Image
from tensorflow.keras.applications import MobileNetV2 # type: ignore
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input # type: ignore
from tensorflow.keras.models import Model # type: ignore

# Load SVM model
model = joblib.load("svm_model.pkl")

# Load MobileNetV2 feature extractor
base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224, 224, 3))
feature_extractor = Model(inputs=base_model.input, outputs=base_model.output)

# UI setup
st.set_page_config(page_title="Cat Dog Predictor", layout="centered")
st.title("🐾 Cat Dog Predictor")
st.write("Upload an image of a **cat or dog** to get a prediction!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Preprocess
    img = image.resize((224, 224))
    img_array = np.array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    # Extract features
    features = feature_extractor.predict(img_array)
    features_flat = features.reshape(1, -1)

    # Predict
    prediction = model.predict(features_flat)[0]
    label = "🐶 Dog" if prediction == 1 else "🐱 Cat"

    st.markdown(f"### Prediction: {label}")
