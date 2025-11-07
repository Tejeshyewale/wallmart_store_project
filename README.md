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

📊 Power BI Dashboard Snapshot

(Include screenshots here when ready — e.g. store sales heatmap, markdown vs. sales chart.)

🌐 Streamlit Web App

📍 Live Demo: [Add Streamlit Cloud Link Here]
📁 GitHub Repository: [Add GitHub Link Here]

🧩 Folder Structure
Walmart_Store_Sales_Forecasting/

├── 📁 data/ # Raw and processed datasets
│   
    ├── train.csv # Training dataset

│    ├── test.csv # Testing dataset

│    ├── features.csv # Additional store and markdown features

│    └── stores.csv # Store metadata and details

├── 📁 notebooks/ # Jupyter notebooks for experimentation

│    ├── EDA.ipynb # Exploratory Data Analysis

│    ├── Model_Training.ipynb # Model building and evaluation

├── 📁 app/ # Streamlit app files

│    ├── app.py # Main Streamlit application

│    ├── model.pkl # Saved trained model (serialized)

│    └── utils.py # Helper functions (if any)

├── 📁 dashboard/ # Power BI assets

│    └── PowerBI_Report.pbix # Power BI report file

├── 📄 README.md # Project overview and documentation

├── 📄 requirements.txt # Python dependencies

└── 📄 Walmart_Store_Sales_Forecasting_Schedule.docx # Project plan document




| Phase  | Description                                           | Duration |
| ------ | ----------------------------------------------------- | -------- |
| Week 1 | Data understanding, cleaning, and feature engineering | 7 days   |
| Week 2 | Model training, tuning, and evaluation                | 7 days   |
| Week 3 | Power BI dashboard creation and publishing            | 7 days   |
| Week 4 | Streamlit app development and deployment              | 7 days   |


✅ Final Deliverables

📂 Cleaned dataset

🧠 Trained ML model (XGBoost)

📊 Power BI Dashboard

🌐 Streamlit Web App

📘 Project Report + README Documentation

🧾 References

Kaggle: Walmart Recruiting - Store Sales Forecasting
Walmart dataset metadata and documentation
