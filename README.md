# data-science-peru-student-enrollment

# Project Overview

This project analyzes student enrollment data from a Peruvian university in 2023. It includes data cleaning, statistical summaries, visualizations, and a basic predictive model to understand enrollment patterns and tuition payment behavior.

---

# Folder Structure

```
project-root/
├── data/
│   └── peru_student_enrollment_data_2023.csv
├── outputs/
│   ├── clean_data.csv
│   ├── summary.txt
│   ├── model_results.txt
│   └── visualizations/
│       ├── enrollment_types.png
│       ├── gender_distribution.png
│       ├── courses_histogram.png
│       └── tuition_heatmap.png
├── scripts/
│   ├── 01_load_and_clean.py
│   ├── 02_summary_statistics.py
│   ├── 03_visualizations.py
│   └── 04_modeling.py
├── requirements.txt
└── README.md
```

---

# Usage

### 1. Setup the Project:

Clone the repository.  
Ensure you have Python installed.  
Install required dependencies using the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 2. Run Scripts:

**Step 1: Load and clean the data**
```bash
python scripts/01_load_and_clean.py
```

**Step 2: Generate summary statistics**
```bash
python scripts/02_summary_statistics.py
```

**Step 3: Create visualizations**
```bash
python scripts/03_visualizations.py
```

**Step 4: Run predictive model**
```bash
python scripts/04_modeling.py
```

---

# Requirements

- Python 3.7+
- pandas
- matplotlib
- seaborn
- scikit-learn

All dependencies can be installed using the `requirements.txt` file.

---

# Acknowledgments

dataset name: Peru Student Enrollment Data (2023)  
dataset author: Miguel Mallqui Diaz  
dataset source: https://www.kaggle.com/datasets/miguelmallqui17/peru-student-enrollment-data-2023