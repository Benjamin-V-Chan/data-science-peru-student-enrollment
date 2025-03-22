import pandas as pd
import os

input_path = "data/peru_student_enrollment_data_2023.csv"
output_path = "outputs/clean_data.csv"
os.makedirs("outputs", exist_ok=True)

df = pd.read_csv(input_path)

df.columns = df.columns.str.strip().str.upper().str.replace(" ", "_")

df['GENDER'] = df['GENDER'].replace({'1': 'M', '2': 'F', 'm': 'M', 'f': 'F'})
df['GENDER'] = df['GENDER'].fillna('U')
df['GENDER'] = df['GENDER'].str.upper()

df = df.fillna('Unknown')

df.to_csv(output_path, index=False)
