# **ProjectCSA2001**

# **AI-Based Expense Analyzer**

## **Project Overview:**
This project is a simple AI-based expense tracker system built using Python. It helps users record their daily expenses, analyze spending patterns, and generate basic AI-based warnings such as overspending and future spending predictions.

The project focuses on applying basic concepts of data analysis and simple AI logic using real-life data.

--

## **Problem Statement:**
Managing daily expenses is difficult, especially for students. Many people don't use money properly which eventually leads to overspending.

This project solves the problem by:
* Recording expenses
* Categorizing spending
* Providing analysis and suggestions

--

## **Features:**
* Add daily expenses
* View total and category-wise spending
* Time-based analysis
* Some AI-based suggestions
* AI-generated report with warnings/messages

--

## **Technologies Used:**

* Python
* Pandas(for handling data)
* CSV File(for storing data)

--

## **Project Structure:**

Project folder contains-
* main.py                         Main program
* M1data_handler.py               Handles data storage (Module 1)
* M2analysis_by_ai.py             Analysis + AI suggestions (Module 2)
* M3time_analysis.py              Time-based analysis (Module 3)
* M4ai_generated_report.py        Generates AI report (Module 4)
* expenses.csv                    Data file(stores data as Amount,Category,Date)
* README.md                       Project documentation

--

## **How to Run the Project?**:

**Step 1: Install Requirements**

Install Python (if not installed) - https://www.python.org

Then install pandas: pip install pandas


**Step 2: Run the Program**

Open terminal in project folder and run:

python main.py

--

## **How to Use?**:

1. Run the program
2. Choose from AI-expenses menu-
   1. Add Expense
   2. View Analysis
   3. Time-based Analysis
   4. AI Report
   5. Exit
3. Enter expense details accordingly.

--

## **AI Concepts Used**:

1. Basic data analysis using pandas
2. Rule-based AI (if-elif-else logic)
3. Classfication of Spending (LOW / MEDIUM / HIGH)
4. Simple Prediction (estimated by taking average)

## **Expected Output**:

-> Total Spending

-> Category-wise Spending

-> Highest Spending Category

-> Daily / Weekday / Monthly Spending

-> AI suggestions and warnings

--

## **Future Improvements**:

1. Can add graphs for visualization.
2. Use Machine Learning Models for prediction.
3. Build a web / mobile interface.
4. Add budget goal tracking

--

## **Learning Outcomes**:

* Understanding real-world problem solving.
* Working with CSV data using pandas
* Applying basic AI/ML concepts.
* Writing modular Python code.

--




