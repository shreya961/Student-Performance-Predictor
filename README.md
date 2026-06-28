#  Student Performance Predictor

A Machine Learning web application built using **Python, Scikit-learn, and Streamlit** that predicts a student's final exam score based on study-related factors.


##  Live Demo

https://student-performance-predictor-uumumbt2ckudascxxhqpvt.streamlit.app/

##  Project Overview

This project uses a **Linear Regression** model to estimate a student's final exam score based on the following input features:

-  Study Hours
-  Attendance (%)
-  Previous Score
-  Sleep Hours
-  Assignments Completed

The trained model is integrated into a **Streamlit** web application, allowing users to enter student details and receive real-time score predictions.

##  Features

- Predicts final exam scores using Machine Learning
- Interactive and user-friendly Streamlit interface
- Real-time predictions
- Performance insights and visualizations
- Clean and responsive UI

##  Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Plotly

##  Project Structure

```
Student-Performance-Predictor/
│── app.py
│── train_model.py
│── utils.py
│── model.pkl
│── student_perf_data.csv
│── requirements.txt
│── README.md
│── .gitignore
```

##  Installation

### Clone the repository

```bash
git clone https://github.com/shreya961/Student-Performance-Predictor.git
```

### Navigate to the project folder

```bash
cd Student-Performance-Predictor
```

### Install the required libraries

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

##  Machine Learning Model

- **Algorithm:** Linear Regression
- **Problem Type:** Regression
- **Target Variable:** Final Exam Score
  
##  Future Improvements

- Add multiple machine learning models for comparison
- Improve prediction accuracy with feature engineering
- Store prediction history
- Deploy with a database backend
- Add user authentication


---

⭐ If you found this project useful, consider giving it a star!
