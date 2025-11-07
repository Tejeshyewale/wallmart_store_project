🛒 Walmart Store Sales Forecasting
📌 Overview

The Walmart Store Sales Forecasting project aims to predict weekly sales for various Walmart stores based on historical data, markdown events, and seasonal patterns.
This project demonstrates an end-to-end data science pipeline, from data preprocessing and feature engineering to model deployment and visualization.

🎯 Objectives

Analyze Walmart’s historical sales data.

Identify factors affecting sales (holidays, markdowns, departments).

Build and train machine learning models to forecast sales.

Create a Power BI dashboard for interactive business insights.

Deploy an interactive web app using Streamlit Cloud for live predictions.

🧠 Project Workflow
1️⃣ Data Understanding & Preprocessing

Loaded and explored the datasets: train.csv, test.csv, features.csv, and stores.csv.

Cleaned missing values, normalized markdown fields, and formatted date columns.

Engineered new features:

Month, Year, WeekOfYear

IsHoliday flag

Rolling averages and lagged sales for trend capture.

2️⃣ Exploratory Data Analysis (EDA)

Analyzed weekly sales trends across stores and departments.

Visualized markdown impacts on holiday and non-holiday sales.

Observed seasonal spikes during Christmas, Thanksgiving, and Labor Day.

3️⃣ Model Building

Trained and compared multiple regression models:

Linear Regression (Baseline)

Random Forest Regressor

XGBoost Regressor

LightGBM

Evaluated models using Root Mean Squared Error (RMSE).

Tuned hyperparameters using GridSearchCV.

Final model: XGBoost (best balance of accuracy and interpretability).

4️⃣ Power BI Dashboard

Created an interactive Power BI dashboard to visualize:

Store-wise weekly sales distribution

Department performance analysis

Holiday impact vs. Normal weeks

Markdown event contribution to sales growth

Time-series trends with filters and slicers

5️⃣ Streamlit Web App Deployment

Built an interactive web app where users can:

Select Store ID, Department, and Week

Get predicted weekly sales

View visualizations (sales trend, markdown effect)

Deployed on Streamlit Cloud for public access.

🛠️ Tools & Technologies
Category	Tools Used
Programming	Python, Pandas, NumPy, Scikit-learn, XGBoost
Visualization	Matplotlib, Seaborn, Power BI
Deployment	Streamlit, Streamlit Cloud
Documentation	Jupyter Notebook, Markdown
Version Control	Git, GitHub
