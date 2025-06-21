# 🤖 Automation Using Python, SQL & Data Science

A complete mini-project that automates a data workflow from SQL extraction to report generation with Python and Machine Learning.

---

## 🚀 What It Does

- 🔌 Extracts data from a SQLite database using `SQLAlchemy`
- 🧼 Cleans and transforms data with `pandas`
- 🤖 Trains a simple `RandomForest` model to predict revenue
- 📊 Generates a monthly revenue chart using `matplotlib`
- ⏱️ Optionally schedules the pipeline with `schedule`

---

## 🗂️ Project Structure

```bash
automation-python-sql-datascience/
├── data/                  # Sample SQLite database
├── scripts/               # Python scripts for each pipeline step
├── reports/               # Output charts
├── automation_runner.py   # Runs entire workflow
├── requirements.txt       # All dependencies
└── README.md              # This file!
