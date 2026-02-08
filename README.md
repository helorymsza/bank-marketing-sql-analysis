# Bank Marketing Campaign Analysis (SQL)

## 📌 Project Overview
This project analyzes the results of a Portuguese bank’s marketing campaigns using SQL and SQLite.
The campaigns were mainly conducted via phone calls, offering clients a term deposit.

The goal is to identify patterns that influence whether a client subscribes to a term deposit and extract actionable business insights.

## 📊 Dataset
The dataset contains information about clients, their demographics, financial status, and campaign contact details.

Main columns include:
- age
- job
- marital
- education
- default
- housing
- loan
- contact
- month
- day_of_week
- campaign outcome (`y`)

Target variable:
- `y`: whether the client subscribed to a term deposit (`yes` or `no`)

## 🔍 Analysis Performed
- Database creation and data import using SQLite
- Exploratory analysis of client demographics
- Campaign outcome analysis
- Identification of factors associated with higher subscription rates

## 📈 Key Insights
- Certain job categories show higher subscription rates
- Clients contacted via cellular tend to subscribe more often
- Campaign timing (month/day) impacts success rates

## ▶️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/helorymsza/bank-marketing-sql-analysis.git
```

### 2. Navigate to the project folder
```bash
cd bank-marketing-sql-analysis
```

### 3. Create the SQLite database
```bash
python3 create_db.py
```

### 4. Open SQLite
```bash
sqlite3 bank_marketing.db
```

### 5. Run exploratory queries
```sql
.read exploratory.sql
.read insights.sql
```

## 🛠️ Technologies Used
SQLite
SQL
Python
Git & GitHub

## Conclusion
- This project demonstrates how SQL can be used to explore marketing data and extract insights that support business decision-making.
- It also serves as a portfolio project showcasing database creation, querying, and analytical thinking.
