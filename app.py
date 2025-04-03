import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load and preprocess dataset
df = pd.read_csv('data/train.txt', sep=';', names=["text", "label"])

# Split data
X = df['text']
y = df['label']

# Vectorize
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

# Streamlit UI
st.set_page_config(page_title="Emotion Tracker", page_icon="🧠")
st.title("🎭 Emotion Detector from Your Text")

st.write("Talk with me and I'll tell you the emotion!")

user_input = st.text_area("✍️ Your text here:")

if st.button("🔍 Detect Emotion"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence.")
    else:
        user_vec = vectorizer.transform([user_input])
        prediction = model.predict(user_vec)[0]
        st.success(f"Predicted Emotion: **{prediction.capitalize()}** 🎯")
