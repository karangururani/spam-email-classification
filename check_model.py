import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')
ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    words = nltk.word_tokenize(text)
    cleaned = []
    for w in words:
        if w.isalnum() and w not in stopwords.words('english'):
            cleaned.append(ps.stem(w))
    return " ".join(cleaned)

tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

test_msg = "Bank account suspended verify now"
cleaned = transform_text(test_msg)
vector = tfidf.transform([cleaned])

print("Cleaned text:", cleaned)
print("Spam probability:", model.predict_proba(vector)[0][1])
print("Prediction:", model.predict(vector)[0])
