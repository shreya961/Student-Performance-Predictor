import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("student_perf_data.csv")

print("Columns:", data.columns)

# Features (based on your dataset)   
X = data[["study_hours", "attendance_percent", "previous_score", "sleep_hours", "assignments_completed"]]
y = data["final_exam_score"]

#x=input  ,y=output

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print(" Model has been trained")