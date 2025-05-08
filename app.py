from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained pipeline (includes preprocessing + model)
with open("HireOrNot.pkl", "rb") as f:
    model_pipeline = pickle.load(f)

# Define the column names as per your model's expectations
numerical_columns = ['Age', 'ExperienceYears', 'PreviousCompanies', 'InterviewScore', 'SkillScore', 'PersonalityScore']
categorical_columns = ['Gender', 'EducationLevel', 'RecruitmentStrategy']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extracting the values from the form
        features = [
            int(request.form['age']),                  # Age
            int(request.form['experience']),           # ExperienceYears
            int(request.form['previous_companies']),   # PreviousCompanies
            int(request.form['interview_score']),      # InterviewScore
            int(request.form['skill_score']),          # SkillScore
            int(request.form['personality_score']),    # PersonalityScore
            int(request.form['gender']),               # Gender (0 or 1)
            int(request.form['education']),            # EducationLevel (1-4)
            int(request.form['recruitment_strategy'])  # RecruitmentStrategy (1-3)
        ]
        
        # Convert to DataFrame
        input_df = pd.DataFrame([features], columns=numerical_columns + categorical_columns)
        
        # Make prediction using the pipeline
        prediction = model_pipeline.predict(input_df)[0]

        # Return the result to the user
        result = "Hired ✅" if prediction == 1 else "Not Hired ❌"
        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
