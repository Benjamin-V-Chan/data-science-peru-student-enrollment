import pandas as pd

df = pd.read_csv("outputs/clean_data.csv")

lines = []

lines.append("Enrollment Types:\n")
lines.append(df['ENROLLMENT'].value_counts().to_string())
lines.append("\n\nTuition Payment March 2023:\n")
lines.append(df['TUITION_PAYMENT_MARCH_2023'].value_counts(normalize=True).to_string())
lines.append("\n\nGender Distribution:\n")
lines.append(df['GENDER'].value_counts().to_string())
lines.append("\n\nStudy Modes:\n")
lines.append(df['STUDY_MODE'].value_counts().to_string())
lines.append("\n\nShifts:\n")
lines.append(df['SHIFT/SCHEDULE'].value_counts().to_string())
lines.append("\n\nCourses Enrolled vs At-Risk:\n")
lines.append(pd.crosstab(df['NUMBER_OF_ENROLLED_COURSES'], df['AT-RISK_COURSE']).to_string())

with open("outputs/summary.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
