
# 🎬 Project 9: Movie Review Sentiment Classifier

This project predicts whether a short movie review is Positive or Negative using TF-IDF and Logistic Regression. Built with scikit-learn and Streamlit.

---

## 🧭 Phase-by-Phase Breakdown

### 🔹 Phase 1: Dataset Creation
- 50 reviews: 25 Positive, 25 Negative
- File: `movie_reviews_dataset.csv`

---

### 🔹 Phase 2: Text Vectorization
- Used `TfidfVectorizer` with stopword removal and lowercase
- Transformed text reviews into numerical vectors

---

### 🔹 Phase 3: Model Training
- Classifier: `Logistic Regression`
- Evaluation: Accuracy, Precision, Recall, F1
- Trained on 80% split
- File: `sentiment_model.joblib`

---

### 🔹 Phase 4: Packaging
- Saved model and vectorizer using `joblib`
- Files:
  - `models/sentiment_model.joblib`
  - `models/tfidf_vectorizer.joblib`

---

### 🔹 Phase 5: Streamlit App
- App UI: Enter review → see predicted sentiment
- File: `app/movie_sentiment_app.py`

---

### 🔹 Phase 6: Hugging Face Deployment
- Prepared deploy folder:
  - `README.md` with config block
  - `requirements.txt`
- Zipped for upload

---

### 🔹 Phase 7: GitHub Deployment
- GitHub-ready ZIP created
- Includes app, models, and documentation

---

## 🎯 Core Components Summary

| Stage           | Tools Used         | Output                          |
|----------------|--------------------|---------------------------------|
| Dataset         | Pandas             | `movie_reviews_dataset.csv`     |
| Text Vector     | TfidfVectorizer    | TF-IDF Matrix                    |
| Model           | LogisticRegression | Sentiment classifier             |
| UI              | Streamlit          | `movie_sentiment_app.py`         |
| Deployment      | Hugging Face       | Streamlit app                    |
| Version Control | GitHub             | Public project repo              |
