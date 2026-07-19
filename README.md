![Python](https://img.shields.io/badge/Python-3.14-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.7-orange)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-brightgreen)

#  House Price Prediction using Machine Learning
Predict house prices using Machine Learning regression models built with Scikit-learn.

A Machine Learning project that predicts house prices using:

- Linear Regression
- Ridge Regression
- Lasso Regression

Dataset:
Kaggle - House Prices: Advanced Regression Techniques

 ## Project Overview

This project predicts house prices using Machine Learning regression models.

The project covers the complete ML workflow, including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Feature Engineering
- Model Training
- Hyperparameter Tuning
- Model Saving
- Price Prediction using a saved model

---

##  Dataset

Dataset: Kaggle House Prices - Advanced Regression Techniques

Files used:

- train.csv
- test.csv
- data_description.txt

---

##  Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Joblib

---

##  Workflow

1. Load Dataset
2. Exploratory Data Analysis (EDA)
3. Handle Missing Values
4. One-Hot Encoding
5. Train-Test Split
6. Feature Scaling
7. Linear Regression
8. Ridge Regression
9. Lasso Regression
10. Hyperparameter Tuning using GridSearchCV
11. Save the Best Model
12. Predict House Prices

---

##  Models Used

- Linear Regression
- Ridge Regression
- Lasso Regression

---

##  Model Performance

| Model | R² Score |
|--------|---------:|
| Linear Regression | 0.8558 |
| Ridge Regression (Best) | 0.8613 |
| Lasso Regression | 0.8405 |

Best Model:
**Ridge Regression**

---

##  Project Structure

```
House-Price-Prediction/

│── data/
│── notebooks/
│── models/
│── predict.py
│── requirements.txt
│── README.md
```

---

##  How to Run

Clone the repository

```bash
git clone <repository-link>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run prediction

```bash
python predict.py
```

---

##  Future Improvements

- Random Forest Regressor
- XGBoost Regressor
- Streamlit Web Application
- Model Deployment

---

## Author

Mohan Krishna C J
B.Tech CSE Student