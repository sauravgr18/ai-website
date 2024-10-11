import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
df = pd.read_csv('student_marks_job_roles_1000.csv')

# Encode the job roles into numerical values using LabelEncoder
label_encoder = LabelEncoder()
df['Job Role'] = label_encoder.fit_transform(df['Job Role'])

# Split the data into features (X) and target (y)
X = df.drop('Job Role', axis=1)
y = df['Job Role']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model's accuracy on the test data
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model to a file
joblib.dump(model, 'career_prediction_model.pkl')

# Save the label encoder (for decoding job roles)
joblib.dump(label_encoder, 'label_encoder.pkl')

print("Model and Label Encoder saved as 'career_prediction_model.pkl' and 'label_encoder.pkl'")
