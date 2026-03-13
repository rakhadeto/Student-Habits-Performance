# 📊 Student Habits & Academic Performance
### Descriptive Analytics Portfolio Project

<p align="center">
  <img src="visualizations/dashboard_overview.png" alt="Dashboard Overview" width="100%"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Type-Descriptive%20Analytics-1F4E79?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Dataset-Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white"/>
  <img src="https://img.shields.io/badge/Records-1%2C000%20Students-ED7D31?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Variables-16%20Features-70AD47?style=for-the-badge"/>
</p>

---

## 📌 Project Overview

This project applies **Descriptive Analytics** to explore the relationship between student lifestyle habits and academic performance. Using a dataset of **1,000 students** with **16 variables**, this analysis answers:

> *"What daily habits and personal factors are most associated with higher exam scores?"*

**Analytics Type Used: Descriptive Analytics**
Descriptive analytics summarizes historical data to reveal patterns, trends, and distributions — answering the question **"What happened?"** It is the foundation of data-driven decision-making and the first step before applying diagnostic, predictive, or prescriptive analytics.

---

## 🗂️ Repository Structure

```
student-habits-performance/
│
├── 📁 data/
│   ├── raw/
│   │   └── student_habits_performance.csv     # Original dataset (Kaggle)
│   └── processed/
│       ├── student_habits_cleaned.csv         # Cleaned + feature-engineered data
│       ├── summary_statistics.csv             # Descriptive statistics
│       ├── correlation_matrix.csv             # Full correlation matrix
│       └── score_distribution.csv             # Score category breakdown
│
├── 📁 notebooks/
│   └── analysis.py                            # Full analysis script (reproducible)
│
├── 📁 visualizations/
│   ├── dashboard_overview.png                 # 6-panel summary dashboard
│   ├── chart1_distribution.png                # Exam score histogram
│   ├── chart2_scatter.png                     # Study hours vs exam score
│   ├── chart3_diet.png                        # Diet quality vs score
│   ├── chart4_heatmap.png                     # Correlation heatmap
│   ├── chart5_boxplot.png                     # Part-time job vs score
│   ├── chart6_parental_edu.png                # Parental education vs score
│   ├── chart7_pie.png                         # Gender distribution
│   ├── chart8_internet_gender.png             # Internet quality & gender
│   ├── chart_score_categories.png             # Score category distribution
│   ├── chart_correlation_ranked.png           # Correlation ranking bar
│   ├── chart_study_intensity.png              # Study intensity analysis
│   ├── chart_pairplot.png                     # Multi-variable pairplot
│   ├── study_mental_health.png                # Mental health analysis
│   └── sleep_exercise.png                     # Sleep & exercise analysis
│
├── 📁 reports/
│   └── Laporan Descriptive Analytics Naufal.docx   # Full Word report (Indonesian)
│
├── requirements.txt
└── README.md
```

---

## 📂 Dataset

| Attribute | Details |
|-----------|---------|
| **Source** | [Kaggle](https://www.kaggle.com) |
| **File** | `student_habits_performance.csv` |
| **Records** | 1,000 students |
| **Features** | 16 variables |
| **Target Variable** | `exam_score` (0–100) |
| **Missing Values** | 91 (in `parental_education_level`) |

### Variable Description

| Variable | Type | Description |
|----------|------|-------------|
| `student_id` | Categorical | Unique student identifier |
| `age` | Numeric | Age of student (17–24) |
| `gender` | Categorical | Male / Female / Other |
| `study_hours_per_day` | Numeric | Average daily study hours |
| `social_media_hours` | Numeric | Daily social media usage (hours) |
| `netflix_hours` | Numeric | Daily Netflix/streaming usage (hours) |
| `part_time_job` | Categorical | Whether student has part-time job |
| `attendance_percentage` | Numeric | Class attendance percentage (%) |
| `sleep_hours` | Numeric | Average nightly sleep hours |
| `diet_quality` | Categorical | Poor / Fair / Good |
| `exercise_frequency` | Numeric | Exercise days per week |
| `parental_education_level` | Categorical | High School / Bachelor / Master |
| `internet_quality` | Categorical | Poor / Average / Good |
| `mental_health_rating` | Numeric | Self-rated mental health (1–10) |
| `extracurricular_participation` | Categorical | Yes / No |
| `exam_score` | Numeric | **Target** — Final exam score (0–100) |

---

## 📊 Key Findings

### 🔑 1. Study Hours is the Dominant Factor (r = 0.825)

<p align="center">
  <img src="visualizations/chart2_scatter.png" width="75%"/>
</p>

Study hours per day has a **very strong positive correlation (r = 0.825)** with exam score — by far the highest among all variables. Students who study 6+ hours/day consistently score above 80.

---

### 📈 2. Correlation Rankings

<p align="center">
  <img src="visualizations/chart_correlation_ranked.png" width="70%"/>
</p>

| Variable | Correlation | Interpretation |
|----------|------------|----------------|
| Study Hours/Day | **+0.825** | Very Strong Positive |
| Mental Health Rating | **+0.322** | Moderate Positive |
| Exercise Frequency | **+0.160** | Weak Positive |
| Sleep Hours | **+0.122** | Weak Positive |
| Attendance % | **+0.090** | Very Weak Positive |
| Netflix Hours | **–0.172** | Weak Negative |
| Social Media Hours | **–0.167** | Weak Negative |

---

### 🧠 3. Mental Health & Study Intensity

<p align="center">
  <img src="visualizations/study_mental_health.png" width="80%"/>
</p>

Students with higher mental health ratings and more intensive study schedules achieve significantly better exam results.

---

### 🥗 4. Lifestyle Factors Matter

<p align="center">
  <img src="visualizations/sleep_exercise.png" width="80%"/>
</p>

Diet quality, sleep habits, and exercise frequency all show positive trends with exam performance — reinforcing the value of a balanced lifestyle.

---

### 🔥 5. Correlation Heatmap

<p align="center">
  <img src="visualizations/chart4_heatmap.png" width="75%"/>
</p>

---

### 📦 6. Score Distribution

<p align="center">
  <img src="visualizations/chart1_distribution.png" width="70%"/>
</p>

| Statistic | Value |
|-----------|-------|
| Mean | 69.60 |
| Median | 70.50 |
| Std Dev | 16.89 |
| Min | 18.4 |
| Max | 100.0 |

<p align="center">
  <img src="visualizations/chart_score_categories.png" width="70%"/>
</p>

---

### 🔍 7. Multi-Variable Pairplot

<p align="center">
  <img src="visualizations/chart_pairplot.png" width="85%"/>
</p>

---

## 🛠️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/student-habits-performance.git
cd student-habits-performance
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Analysis
```bash
cd notebooks
python analysis.py
```
All charts will be saved to `visualizations/` and processed data to `data/processed/`.

---

## 📦 Requirements

```
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
```

---

## 💡 Analytical Approach

This project uses **Descriptive Analytics**, which:
- Summarizes historical data using statistical measures (mean, median, std dev, percentages)
- Identifies patterns and correlations between variables
- Presents findings through informative visualizations
- Does **not** predict future outcomes (that would be Predictive Analytics)
- Does **not** explain root causes (that would be Diagnostic Analytics)

---

## ❓ Q&A Section

### Q1: Why is it important to identify the question before beginning the project?

Defining a clear analytical question before starting is critical because it:
- **Focuses the analysis** — prevents wasting time on irrelevant data explorations
- **Guides method selection** — the question determines which analytics type (descriptive, diagnostic, predictive, prescriptive) is appropriate
- **Saves resources** — avoids collecting/cleaning data that won't be used
- **Enables measurement of success** — you know when the analysis is "done"
- **Improves communication** — stakeholders understand the output when it directly answers a stated question

In this project, the guiding question was: *"What habits are most associated with higher exam scores?"* — which directed every analytical and visualization decision.

### Q2: Sources of Open Data for Analysis

The dataset for this project was downloaded from **[Kaggle](https://www.kaggle.com)**.

Other notable open data sources include:

| Source | URL | Description |
|--------|-----|-------------|
| **Kaggle** ⭐ *(used here)* | kaggle.com | Thousands of datasets across all domains |
| **UCI ML Repository** | archive.ics.uci.edu | Classic ML & statistics datasets |
| **Google Dataset Search** | datasetsearch.research.google.com | Search engine for datasets |
| **Data.gov** | data.gov | US government open data |
| **World Bank Open Data** | data.worldbank.org | Global economic & social data |
| **Our World in Data** | ourworldindata.org | Global development & health data |
| **Statista** | statista.com | Industry statistics & surveys |

---

## 📄 License

This project is for educational and portfolio purposes. Dataset originally from Kaggle.

---

<p align="center">
  Made with ❤️ using Python · pandas · matplotlib · seaborn
</p>
