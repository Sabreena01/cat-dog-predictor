# cat-dog-predictor
This project is a machine learning-based image classifier built using a Support Vector Machine (SVM) model. It predicts whether an uploaded image is of a cat or a dog, using features extracted from images. The model achieves high accuracy (~98%) on unseen data.
A simple and accurate image classification web app that predicts whether an uploaded image is of a **cat** or a **dog** using an **SVM (Support Vector Machine)** model and a custom-built **Streamlit UI**.

- ✅ Trained using MobileNetV2 feature extraction
- ✅ Achieved **98% accuracy** on unseen test data
- ✅ Lightweight and fast — no deep learning required!

---

## 📸 Demo

![Demo Screenshot](demo_screenshot.png) 
<img width="953" alt="demo_screenshot" src="https://github.com/user-attachments/assets/3c269e33-83a9-4d33-bd2a-e1059fc00ef8" />

---

## 🚀 Features

- Upload a cat or dog image from your system
- Instantly see prediction results
- Simple, clean and custom-designed UI built with **Streamlit**
- Accurate prediction using pre-trained SVM model

---

## 🧠 Model Details

- **Model Type:** SVM (Support Vector Machine)
- **Feature Extractor:** MobileNetV2 (Pretrained, `imagenet`)
- **Input Shape:** 224 x 224 x 3
- **Training Accuracy:** 98%
- **Frameworks Used:** TensorFlow (for feature extraction), Scikit-learn (for SVM)

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sabreena01/cat-dog-predictor.git
cd cat-dog-predictor

## 2.Install Dependencies
pip install -r requirements.txt
git lfs install
git lfs pull

▶️ Running the App
streamlit run main.py

🧪 Example Output
Upload image of a cat:
✅ Prediction: Cat

Upload image of a dog:
✅ Prediction: Dog

📂 Project Structure
cat-dog-predictor/
├── main.py                 # Streamlit app code
├── model.pkl               # Trained SVM model (handled by Git LFS)
├── requirements.txt        # Python dependencies
├── README.md               # This file

🧠 Future Improvements
Deploy the app online using Streamlit Cloud
Add batch prediction feature
Extend the model to multiple pet types (e.g., rabbit, bird)
Add webcam-based predictions

📢 Author
Sabreena
📫 GitHub: @Sabreena01

📝 License
This project is open source and free to use under the MIT License.






