# Spam Email Classification System

This project is a Machine Learning based **Spam Email Classification System** developed using **Python**, **Flask**, and **Scikit-learn**.  
It predicts whether a given email or message is **Spam** or **Not Spam**.

---

## 🔹 Project Description

Spam emails are unwanted messages that usually contain advertisements, fake offers, or phishing attempts.  
This project uses Machine Learning techniques to automatically detect spam emails based on their content.

The model is trained using the **SMS Spam Collection Dataset** and deployed as a web application using Flask.

---

## 🔹 Features

- Classifies messages as **Spam** or **Not Spam**
- Uses **TF-IDF Vectorization**
- Uses **Logistic Regression** for classification
- Web-based interface using Flask
- Simple and beginner-friendly implementation

---

## 🔹 Technologies Used

- Python  
- Flask  
- Scikit-learn  
- Pandas  
- HTML, CSS  
- Git & GitHub  

---

## 🔹 Project Structure
Spam-Email-Classification/
│
├── app.py
├── train_model.py
├── check_model.py
├── spam.csv
├── model.pkl
├── vectorizer.pkl
├── Message.txt
│
├── templates/
│ ├── index.html
│ ├── result.html
│ ├── about.html
│ ├── home.html
│
├── static/
│ ├── index.css
│ ├── index.js
│ ├── responsive.css
│
└── README.md

---

## 🔹 How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/karangururani/spam-email-classification.git
cd spam-email-classification

2️⃣ Install Required Libraries
pip install flask pandas scikit-learn

3️⃣ Train the Model
python train_model.py
This will generate:
model.pkl
vectorizer.pkl

4️⃣ Run the Flask Application
python app.py

5️⃣ Open in Browser
http://127.0.0.1:5000/

🧪 Example Spam Messages
Bank account suspended verify now
Congratulations you won a free prize
Claim your reward immediately
Urgent login detected

✅ Output
Spam
Not Spam

📌 Use Case
This project can be used as:
College Mini Project
Machine Learning Practice Project
Resume Project
GitHub Portfolio Project

👤 Author
Karan Gururani


