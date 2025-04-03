# 🎭 Emotion Detection from Text

This project is a simple Machine Learning-based **Emotion Detector** that classifies short text into emotional categories like joy, anger, sadness, love, fear, and surprise. Built using **Scikit-learn** for training and **Streamlit** for a web-based user interface.

---

## 🛠️ Technologies Used

- Python
- Streamlit (for the web app)
- Pandas
- Scikit-learn
- NLTK (for natural language processing)

---

## 📂 Project Structure

```
emotionTracker/
├── data/
│   └── train.txt              # Semicolon-separated emotion dataset
├── emotionTracker.ipynb     # Jupyter Notebook (model training & testing)
├── app.py                    # Streamlit app
├── requirements.txt          # Required Python libraries
└── README.md                 # Project overview
```

---

## 📥 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/emotion-tracker.git
   cd emotion-tracker
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

---

## 🧪 Dataset

The dataset is from [Kaggle: Emotion Detection from Text](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp)

Each line is formatted as:
```
text;label
```

Example:
```
i feel amazing;joy
this is so frustrating;anger
```

---

## 💻 How It Works

- Text is vectorized using **TfidfVectorizer**
- Model is trained using **Logistic Regression**
- User input is passed through the model to return a predicted emotion

---

## 🖼️ Example UI

![Example UI](https://github.com/yourusername/emotion-tracker/assets/example-ui.png)

---

## 🎯 Example Usage

```
Input: I’m so proud of you!
Output: joy
```

```
Input: This makes me furious.
Output: anger
```

---

## ✨ Future Improvements

- Add emoji visualization based on predicted emotion
- Export trained model using `joblib` or `pickle`
- Deploy live via [Streamlit Cloud](https://streamlit.io/cloud)

---

## 👨‍💻 Author

- Created by [Ameera Thiwanka](https://github.com/AmeeraTD)

---

