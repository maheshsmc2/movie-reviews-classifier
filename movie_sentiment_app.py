
import streamlit as st
import joblib

st.title("🎬 Movie Review Sentiment Classifier")

review = st.text_area("Enter a short movie review:")

if review:
    model = joblib.load("models/sentiment_model.joblib")
    vectorizer = joblib.load("models/tfidf_vectorizer.joblib")
    vec = vectorizer.transform([review])
    pred = model.predict(vec)[0]
    st.success(f"📝 Predicted Sentiment: {pred}")
