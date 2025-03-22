import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

df = pd.read_csv("outputs/clean_data.csv")

X = df[['GENDER', 'ENROLLMENT', 'STUDY_MODE', 'SHIFT/SCHEDULE', 'NUMBER_OF_ENROLLED_COURSES']]
X = pd.get_dummies(X, drop_first=True)
y = df['TUITION_PAYMENT_MARCH_2023']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

with open("outputs/model_results.txt", "w") as f:
    f.write(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}\n\n")
    f.write("Classification Report:\n")
    f.write(classification_report(y_test, y_pred))
