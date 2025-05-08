# Hire Or Not – AI-Based Hiring Recommendation System

![License](https://img.shields.io/badge/license-MIT-green) ![Python](https://img.shields.io/badge/Python-3.10-blue)

## 🔍 Overview

**Hire Or Not** is an intelligent machine learning-based hiring recommendation system designed to assist HR professionals and recruiters in evaluating potential candidates. By analyzing various applicant parameters such as education, experience, interview score, and more, the system predicts whether a candidate should be hired or not.

This project implements multiple machine learning algorithms and selects the best-performing model using a comprehensive evaluation process. The selected model is then integrated into an easy-to-use interface for practical use.

## 🚀 Features

- 🧪 Multiple ML models: Random Forest, Gradient Boosting, AdaBoost, Logistic Regression, KNN
- ✅ Automatic model selection based on accuracy
- 📈 Performance evaluation and comparison of models
- 💾 Model deployment using a simple web interface
- 🧩 User-friendly prediction form
- 📊 Real-time hiring decision recommendation

## 🧾 Input Features

The model uses the following candidate attributes for prediction:

- `Age` (20–50)
- `Gender` (0 = Male, 1 = Female)
- `Education Level`  
  - 1 = B.Sc.  
  - 2 = B-Tech  
  - 3 = Master's  
  - 4 = PhD  
- `Experience Years` (0–15)
- `Previous Companies Worked` (1–5)
- `Interview Score` (0–100)
- `Skill Score` (0–100)
- `Personality Score` (0–100)
- `Recruitment Strategy`  
  - 1 = Aggressive  
  - 2 = Moderate  
  - 3 = Conservative

The **target variable** is `Hiring Decision`:  
- 1 = Hired  
- 0 = Not Hired

## 🧰 Technologies Used

- Python 3.10+
- scikit-learn
- pandas, numpy
- matplotlib, seaborn
- Flask (for web interface)
- pickle (for model serialization)

## 📁 Project Structure

```
Hire Or Not/
│
├── static/
│   └── style.css           # Stylesheet for the web interface
│
├── templates/
│   └── index.html          # HTML form for user input
│
├── HirOrNot.pkl            # Saved ML model
├── app.py                  # Flask app script
├── program.ipynb           # Programmed code for EDA and model building
├── requirements.txt        # List of required packages
└── README.md               # Project documentation
```

## 🚦 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/Hire-Or-Not.git
cd Hire-Or-Not
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the application**

```bash
python app.py
```

4. Open your browser and go to `http://127.0.0.1:5000`

## 📄 License

This project is licensed under the **MIT License**. Feel free to use and modify it for your needs.

