# 💳 Credit Scoring Model

## CodeAlpha Machine Learning Internship

### 📌 Project Overview

The Credit Scoring Model is a machine learning project developed to predict the creditworthiness of loan applicants based on their financial and personal information. The model helps identify whether an individual is likely to default on a loan, enabling financial institutions to make informed lending decisions and reduce credit risk.

---

## 🎯 Objective

To build and evaluate machine learning models that can accurately classify loan applicants as low-risk or high-risk borrowers using historical credit-related data.

---

## 📊 Dataset Information

The dataset contains customer financial and credit history information, including:

* Person Age
* Annual Income
* Home Ownership Status
* Employment Length
* Loan Intent
* Loan Grade
* Loan Amount
* Interest Rate
* Loan Percent Income
* Previous Default History
* Credit History Length

**Target Variable:**

* `0` → Low Credit Risk
* `1` → High Credit Risk

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Joblib

---

## 🔍 Machine Learning Workflow

### 1. Data Preprocessing

* Handling missing values
* Data cleaning
* Encoding categorical variables
* Feature selection

### 2. Exploratory Data Analysis (EDA)

* Loan Status Distribution
* Loan Intent Analysis
* Age Distribution
* Income Distribution
* Correlation Matrix

### 3. Model Development

The following machine learning algorithms were implemented:

#### Logistic Regression

A baseline classification model used for credit risk prediction.

#### Random Forest Classifier

An ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

---

## 📈 Model Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix

---

## 🏆 Results

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 82.88%   |
| Random Forest       | 92.97%   |

### Final Model Performance

* Accuracy: **92.97%**
* ROC-AUC Score: **93.49%**

The Random Forest Classifier achieved the highest performance and was selected as the final model.

---

## 🌐 Streamlit Web Application

A user-friendly Streamlit application was developed to allow users to enter customer information and predict credit risk in real time.

### Features

* Interactive user interface
* Real-time credit risk prediction
* Professional and responsive design
* Easy deployment and usage

---

## 📂 Project Structure

```text
CodeAlpha_CreditScoringModel/
│
├── dataset/
│   └── credit_risk_dataset.csv
│
├── Credit_Scoring_Model.ipynb
├── app.py
├── credit_scoring_model.pkl
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 🚀 How to Run the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Jupyter Notebook

```bash
jupyter notebook
```

### Launch Streamlit Application

```bash
streamlit run app.py
```

---

## 📌 Conclusion

This project demonstrates the application of machine learning techniques in the financial domain for credit risk assessment. By leveraging historical customer information, the developed model can effectively identify potential loan defaulters and support better decision-making in loan approval processes.

The Random Forest model delivered excellent predictive performance with an accuracy of 92.97% and a ROC-AUC score of 93.49%, making it a reliable solution for credit scoring.

---

## 👩‍💻 Author

**Dishmitha**


CodeAlpha Machine Learning Internship
