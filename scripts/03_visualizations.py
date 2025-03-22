import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("outputs/clean_data.csv")
os.makedirs("outputs/visualizations", exist_ok=True)

df['ENROLLMENT'].value_counts().plot(kind='bar', title='Enrollment Types')
plt.tight_layout()
plt.savefig("outputs/visualizations/enrollment_types.png")
plt.clf()

df['GENDER'].value_counts().plot(kind='pie', title='Gender Distribution', autopct='%1.1f%%')
plt.tight_layout()
plt.savefig("outputs/visualizations/gender_distribution.png")
plt.clf()

df['NUMBER_OF_ENROLLED_COURSES'].hist(bins=15)
plt.title("Number of Enrolled Courses")
plt.xlabel("Courses")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("outputs/visualizations/courses_histogram.png")
plt.clf()

pivot = pd.crosstab(df['TUITION_PAYMENT_MARCH_2022'], df['TUITION_PAYMENT_MARCH_2023'])
sns.heatmap(pivot, annot=True, fmt="d", cmap="Blues")
plt.title("Tuition Payment: 2022 vs 2023")
plt.tight_layout()
plt.savefig("outputs/visualizations/tuition_heatmap.png")
plt.clf()
