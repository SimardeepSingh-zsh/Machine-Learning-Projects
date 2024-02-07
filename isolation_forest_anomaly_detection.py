import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from joblib import dump, load

# Function to load data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Function to save model
def save_model(model, file_name):
    dump(model, file_name)

# Function to load model
def load_model(file_name):
    model = load(file_name)
    return model

# Load your dataset
file_path = 'data.csv'
X = load_data(file_path)

# Standardize the data
sc = StandardScaler()
X = sc.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Train the model
clf = IsolationForest(contamination=0.01)
clf.fit(X_train)

# Save the trained model
save_model(clf, 'isolation_forest_model.joblib')

# Load the trained model
clf = load_model('isolation_forest_model.joblib')

# Predict the anomalies in the data
pred = clf.predict(X_test)

# Print the anomaly prediction (-1 is an anomaly, 1 is normal)
print(pred)
