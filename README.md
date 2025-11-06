# wallmart_store_project
To build a machine learning model that can accurately forecast weekly sales for every store + department combination.  This helps Walmart:  Plan inventory (how much stock to order),  Adjust staffing levels,  Schedule markdowns (discounts) more effectively,  And improve profits during holidays and special events.


### 📊 Predicting Weekly Sales for Walmart Stores using Machine Learning

---

## 📘 Project Overview

This project aims to **forecast weekly sales** for 45 Walmart stores across various departments using historical sales data.  
It is inspired by the **Walmart Recruiting - Store Sales Forecasting competition on Kaggle**, where the goal was to predict the impact of **markdown events and holidays** on store sales.

Accurate sales forecasting helps Walmart:
- Optimize inventory management 🏬  
- Schedule staff efficiently 👥  
- Plan promotional markdowns effectively 💸  
- Improve customer satisfaction 😊  

---

## 🎯 Problem Statement

Walmart needs to **predict future weekly sales** for each store and department.  
The challenge lies in:
- Limited historical data (few years only)
- Impact of **holiday events** like Christmas, Thanksgiving, etc.
- Effects of **markdowns (discounts)** on specific departments

---

## 🧠 Objective

Build a **machine learning model** that predicts the `Weekly_Sales` for each `(Store, Department, Date)` combination  
and evaluate it using **Weighted Mean Absolute Error (WMAE)**, where holiday weeks are given higher importance.

---

## 🧾 Dataset Information

The dataset consists of historical sales data from **45 Walmart stores** located in different regions.  
Each store contains multiple departments and several influencing factors.

| Feature | Description |
|----------|--------------|
| **Store** | Store ID number |
| **Dept** | Department number |
| **Date** | Week of sales |
| **Weekly_Sales** | Total sales for the department in that week *(Target)* |
| **IsHoliday** | Boolean: whether the week includes a holiday |
| **Temperature** | Average temperature in the region |
| **Fuel_Price** | Cost of fuel in the region |
| **CPI** | Consumer Price Index |
| **Unemployment** | Unemployment rate in the region |
| **Markdown1–5** | Promotional discounts applied |

---

## ⚙️ Evaluation Metric

The competition uses **Weighted Mean Absolute Error (WMAE)**:

\[
WMAE = \frac{\sum_{i=1}^{n} w_i \times |y_i - \hat{y}_i|}{\sum_{i=1}^{n} w_i}
\]

Where:  
- \(y_i\): Actual sales  
- \(\hat{y}_i\): Predicted sales  
- \(w_i\): Weight (5 for holiday weeks, 1 otherwise)

---

## 🧩 Project Workflow

### 1️⃣ Data Collection
- Downloaded dataset from [Kaggle Walmart Sales Forecasting Competition](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)

### 2️⃣ Data Preprocessing
- Handled missing values in Markdown columns  
- Converted `Date` column to datetime format  
- Created new features like `Year`, `Month`, `WeekOfYear`, and `IsHoliday (0/1)`  
- Normalized numerical features

### 3️⃣ Exploratory Data Analysis (EDA)
- Visualized sales trends using Matplotlib and Seaborn  
- Compared sales during holiday vs. non-holiday weeks  
- Analyzed correlation between markdowns and sales  
- Checked store and department performance patterns

### 4️⃣ Feature Engineering
- Created lag features (e.g., previous week’s sales)
- Added interaction features like `Markdown × Holiday`
- Encoded categorical variables if needed

### 5️⃣ Model Building
Implemented and compared several regression models:
- Linear Regression  
- Random Forest Regressor  
- XGBoost Regressor  
- LightGBM (optional advanced model)

### 6️⃣ Model Evaluation
- Used **Weighted MAE** for evaluation  
- Performed hyperparameter tuning using GridSearchCV  
- Compared model performances and selected the best one

### 7️⃣ Prediction & Submission
- Predicted weekly sales for test data  
- Created submission file in the format:
