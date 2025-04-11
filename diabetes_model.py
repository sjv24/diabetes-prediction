# diabetes_logic.py

import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm

# Load the data
df = pd.read_csv('diabetes.csv')

# Prepare input and output
X = df.drop(columns='Outcome', axis=1)
Y = df['Outcome']

# Standardize input features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, stratify=Y, random_state=100)

# Train the model
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Save the model and scaler
pickle.dump(classifier, open('diabetes_model.sav', 'wb'))
pickle.dump(scaler, open('scaler.sav', 'wb'))

print("✅ Model and Scaler saved successfully.")
