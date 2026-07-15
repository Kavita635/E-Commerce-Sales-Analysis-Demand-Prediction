# E-Commerce Sales Analysis & Demand Prediction

## Project Overview

This project focuses on analyzing historical e-commerce sales data and predicting future product demand using Machine Learning. The system helps businesses understand sales trends, identify high-demand products, and make inventory decisions based on predicted demand.

A Random Forest Regression model is trained on the DataCo Supply Chain Dataset to forecast product demand. Based on the predicted demand, the system automatically classifies products into demand levels and provides inventory recommendations such as increasing, maintaining, or reducing stock.

The project also includes an interactive Streamlit dashboard for visualizing predictions, searching products, and exploring demand-related insights.


## Objectives

- Analyze historical e-commerce sales data.
- Perform data preprocessing and feature engineering.
- Train and evaluate multiple Machine Learning models.
- Predict future product demand.
- Classify products into demand levels.
- Generate inventory recommendations.
- Build an interactive Streamlit dashboard for visualization.


## Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Comparison
- Demand Prediction using Random Forest Regressor
- Inventory Recommendation System
- Product Search Dashboard
- Interactive Data Visualizations
- Demand Forecast Export as CSV


## Dataset

**Dataset:** DataCo Supply Chain Dataset

The dataset contains information related to:

- Customer Details
- Product Information
- Sales Records
- Shipping Details
- Delivery Information
- Profit Analysis
- Order Information

The processed dataset is used for model training while the original dataset is used to display readable product information in the dashboard.


## Machine Learning Models Used

- Linear Regression
- Random Forest Regressor

The Random Forest Regressor achieved better performance and was selected as the final prediction model.


## Project Workflow

1. Data Understanding
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Demand Forecasting
8. Streamlit Dashboard Development


## Folder Structure

Ecommerce_Demand_Prediction/
│
├── data/
├── images/
├── models/
├── reports/
├── results/
├── src/
│   ├── 01_data_understanding.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda.py
│   ├── 04_feature_engineering.py
│   ├── 05_model_training.py
│   ├── 06_model_evaluation.py
│   └── 07_demand_forecasting.py
│
├── app.py
├── requirements.txt
└── README.md
```


## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit


## Results

The project successfully:

- Predicted future product demand.
- Classified products into High, Medium, and Low demand.
- Generated inventory recommendations.
- Built an interactive dashboard for product search and visualization.


## Dashboard

The Streamlit dashboard includes:

- Project Summary
- Product Search
- Demand Prediction
- Inventory Recommendation
- Demand Distribution
- Shipping Mode Analysis
- Top Predicted Products


## Future Scope

- Real-time demand prediction
- Deep Learning based forecasting
- Sales trend forecasting
- Cloud deployment
- Business Intelligence integration


## Developer

**Kavita Seervi**

B.Tech Computer Science & Engineering (Data Science)

Manipal University Jaipur