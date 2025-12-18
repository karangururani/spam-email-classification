from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    msg = request.form['message']
    vector = tfidf.transform([msg])
    prob = model.predict_proba(vector)[0][1]

    prediction = "Spam" if prob > 0.5 else "Not Spam"
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
