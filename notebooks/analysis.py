"""
=============================================================
 Student Habits & Academic Performance — Descriptive Analysis
 Author  : Data Analyst Portfolio Project
 Dataset : student_habits_performance.csv (Kaggle)
 Type    : Descriptive Analytics
=============================================================
"""

# ── 0. Imports ────────────────────────────────────────────────────────────────
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import os

# ── 1. Load Data ──────────────────────────────────────────────────────────────
RAW_PATH  = '../data/raw/student_habits_performance.csv'
OUT_DATA  = '../data/processed/'
OUT_VIZ   = '../visualizations/'

os.makedirs(OUT_DATA, exist_ok=True)
os.makedirs(OUT_VIZ,  exist_ok=True)

df = pd.read_csv(RAW_PATH)
print(f"Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")
print(df.head())

# ── 2. Data Cleaning & Feature Engineering ────────────────────────────────────
df_clean = df.copy()

# Fill missing parental education
df_clean['parental_education_level'] = df_clean['parental_education_level'].fillna('Unknown')

# Derived columns
df_clean['score_category'] = pd.cut(
    df_clean['exam_score'],
    bins=[0, 40, 60, 75, 90, 100],
    labels=['Very Low', 'Low', 'Average', 'High', 'Excellent']
)

df_clean['screen_time_total'] = (
    df_clean['social_media_hours'] + df_clean['netflix_hours']
)

df_clean['study_intensity'] = pd.cut(
    df_clean['study_hours_per_day'],
    bins=[-0.1, 2, 4, 6, 8.5],
    labels=['Low (<2h)', 'Moderate (2-4h)', 'High (4-6h)', 'Intense (>6h)']
)

df_clean['sleep_group'] = pd.cut(
    df_clean['sleep_hours'],
    bins=[3, 5, 6, 7, 8, 10],
    labels=['<5h', '5-6h', '6-7h', '7-8h', '>8h']
)

# Save cleaned data
df_clean.to_csv(f'{OUT_DATA}student_habits_cleaned.csv', index=False)

# ── 3. Summary Statistics ─────────────────────────────────────────────────────
print("\n── Summary Statistics ──")
summary = df_clean.describe().round(3)
print(summary)
summary.to_csv(f'{OUT_DATA}summary_statistics.csv')

# Correlation with exam_score
numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
corr_df = df_clean[numeric_cols].corr().round(4)
corr_df.to_csv(f'{OUT_DATA}correlation_matrix.csv')

print("\n── Correlation with Exam Score ──")
print(corr_df['exam_score'].sort_values(ascending=False).to_string())

# Key group stats
print("\n── Avg Score by Gender ──")
print(df_clean.groupby('gender')['exam_score'].agg(['mean','median','count']).round(2))

print("\n── Avg Score by Diet Quality ──")
print(df_clean.groupby('diet_quality')['exam_score'].agg(['mean','median','count']).round(2))

print("\n── Avg Score by Part-Time Job ──")
print(df_clean.groupby('part_time_job')['exam_score'].agg(['mean','median','count']).round(2))

print("\n── Score Category Distribution ──")
score_dist = (
    df_clean['score_category']
    .value_counts()
    .reindex(['Very Low', 'Low', 'Average', 'High', 'Excellent'])
    .reset_index()
)
score_dist.columns = ['category', 'count']
score_dist['percentage'] = (score_dist['count'] / len(df_clean) * 100).round(2)
score_dist.to_csv(f'{OUT_DATA}score_distribution.csv', index=False)
print(score_dist)

# ── 4. Visualization Setup ────────────────────────────────────────────────────
BLUE       = '#1F4E79'
MED_BLUE   = '#2E75B6'
LIGHT_BLUE = '#BDD7EE'
ORANGE     = '#ED7D31'
GREEN      = '#70AD47'
RED        = '#C00000'
GRAY       = '#595959'
BG         = '#F8F9FA'

def save_fig(name):
    plt.savefig(f'{OUT_VIZ}{name}.png', dpi=150, bbox_inches='tight', facecolor=BG)
    plt.close()
    print(f"  ✓ Saved: {name}.png")

# ── 5. Chart 1 — Exam Score Distribution ─────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG); ax.set_facecolor(BG)
ax.hist(df_clean['exam_score'], bins=25, color=MED_BLUE, edgecolor='white', linewidth=0.8)
ax.axvline(df_clean['exam_score'].mean(), color=ORANGE, linestyle='--', linewidth=2,
           label=f"Mean: {df_clean['exam_score'].mean():.1f}")
ax.axvline(df_clean['exam_score'].median(), color=GREEN, linestyle='--', linewidth=2,
           label=f"Median: {df_clean['exam_score'].median():.1f}")
ax.set_title('Distribution of Exam Scores', fontsize=14, fontweight='bold', color=BLUE, pad=15)
ax.set_xlabel('Exam Score', fontsize=11, color=GRAY)
ax.set_ylabel('Number of Students', fontsize=11, color=GRAY)
ax.legend(fontsize=10)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout(); save_fig('chart1_distribution')

# ── 6. Chart 2 — Study Hours vs Exam Score ───────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG); ax.set_facecolor(BG)
sc = ax.scatter(df_clean['study_hours_per_day'], df_clean['exam_score'],
                alpha=0.5, c=df_clean['exam_score'], cmap='Blues', s=25)
z = np.polyfit(df_clean['study_hours_per_day'], df_clean['exam_score'], 1)
xl = np.linspace(df_clean['study_hours_per_day'].min(), df_clean['study_hours_per_day'].max(), 100)
ax.plot(xl, np.poly1d(z)(xl), color=ORANGE, linewidth=2,
        label=f'r = {df_clean["study_hours_per_day"].corr(df_clean["exam_score"]):.3f}')
plt.colorbar(sc, ax=ax, label='Exam Score')
ax.set_title('Study Hours per Day vs Exam Score', fontsize=14, fontweight='bold', color=BLUE, pad=15)
ax.set_xlabel('Study Hours per Day', fontsize=11, color=GRAY)
ax.set_ylabel('Exam Score', fontsize=11, color=GRAY)
ax.legend(fontsize=10)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout(); save_fig('chart2_scatter')

# ── 7. Chart 3 — Correlation Heatmap ─────────────────────────────────────────
cols_for_corr = ['study_hours_per_day', 'social_media_hours', 'netflix_hours',
                 'attendance_percentage', 'sleep_hours', 'exercise_frequency',
                 'mental_health_rating', 'exam_score']
labels_corr   = ['Study Hrs', 'Social Media', 'Netflix', 'Attendance',
                 'Sleep Hrs', 'Exercise', 'Mental Health', 'Exam Score']
corr_m = df_clean[cols_for_corr].corr()
fig, ax = plt.subplots(figsize=(9, 7), facecolor=BG); ax.set_facecolor(BG)
mask = np.zeros_like(corr_m, dtype=bool)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(corr_m, mask=mask, annot=True, fmt='.2f', cmap='Blues',
            ax=ax, linewidths=0.5, vmin=-1, vmax=1,
            xticklabels=labels_corr, yticklabels=labels_corr,
            annot_kws={'size': 9})
ax.set_title('Correlation Matrix of Student Variables', fontsize=14,
             fontweight='bold', color=BLUE, pad=15)
plt.xticks(rotation=45, ha='right', fontsize=9)
plt.yticks(rotation=0, fontsize=9)
plt.tight_layout(); save_fig('chart4_heatmap')

# ── 8. Chart 4 — Score Category Distribution ─────────────────────────────────
cats = df_clean['score_category'].value_counts().reindex(
    ['Very Low', 'Low', 'Average', 'High', 'Excellent'])
fig, ax = plt.subplots(figsize=(8, 5), facecolor=BG); ax.set_facecolor(BG)
bar_colors = [RED, ORANGE, '#FFC000', MED_BLUE, BLUE]
bars = ax.bar(cats.index, cats.values, color=bar_colors, edgecolor='white', width=0.6)
for bar, val in zip(bars, cats.values):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+2,
            f'{val}\n({val/len(df_clean)*100:.1f}%)',
            ha='center', fontsize=9, fontweight='bold', color=GRAY)
ax.set_title('Students by Exam Score Category', fontsize=14, fontweight='bold', color=BLUE, pad=15)
ax.set_xlabel('Score Category', fontsize=11, color=GRAY)
ax.set_ylabel('Number of Students', fontsize=11, color=GRAY)
ax.set_ylim(0, 450)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout(); save_fig('chart_score_categories')

# ── 9. Chart 5 — Correlation Bar (ranked) ────────────────────────────────────
var_list    = ['study_hours_per_day', 'mental_health_rating', 'exercise_frequency',
               'sleep_hours', 'attendance_percentage', 'netflix_hours', 'social_media_hours']
var_labels  = ['Study Hours', 'Mental Health', 'Exercise', 'Sleep',
               'Attendance', 'Netflix', 'Social Media']
corr_vals   = [df_clean[v].corr(df_clean['exam_score']) for v in var_list]
sorted_pairs = sorted(zip(corr_vals, var_labels), key=lambda x: x[0])
c_sorted, l_sorted = zip(*sorted_pairs)
fig, ax = plt.subplots(figsize=(8, 5), facecolor=BG); ax.set_facecolor(BG)
bar_colors2 = [GREEN if c > 0 else RED for c in c_sorted]
bars = ax.barh(l_sorted, c_sorted, color=bar_colors2, edgecolor='white', height=0.6)
ax.axvline(0, color=GRAY, linewidth=0.8)
for bar, val in zip(bars, c_sorted):
    ax.text(val + (0.01 if val >= 0 else -0.01),
            bar.get_y()+bar.get_height()/2,
            f'{val:+.3f}',
            va='center', ha='left' if val >= 0 else 'right',
            fontsize=9, fontweight='bold', color=GRAY)
ax.set_title('Variables Ranked by Correlation with Exam Score',
             fontsize=13, fontweight='bold', color=BLUE, pad=15)
ax.set_xlabel('Pearson Correlation Coefficient', fontsize=10, color=GRAY)
ax.spines['top'].set_visible(False); ax.spines['right'].set_visible(False)
plt.tight_layout(); save_fig('chart_correlation_ranked')

# ── 10. Chart 6 — Study Intensity Group ──────────────────────────────────────
si_avg = df_clean.groupby('study_intensity')['exam_score'].mean()
si_cnt = df_clean['study_intensity'].value_counts().reindex(si_avg.index)
fig, axes = plt.subplots(1, 2, figsize=(12, 5), facecolor=BG)
for ax in axes: ax.set_facecolor(BG)
axes[0].bar(si_avg.index, si_avg.values,
            color=[LIGHT_BLUE, MED_BLUE, BLUE, '#0D2B47'],
            edgecolor='white', width=0.55)
for i, (idx, val) in enumerate(si_avg.items()):
    axes[0].text(i, val+0.5, f'{val:.1f}', ha='center', fontsize=11, fontweight='bold', color=GRAY)
axes[0].set_title('Avg Exam Score by Study Intensity', fontsize=12, fontweight='bold', color=BLUE)
axes[0].set_xlabel('Study Intensity Group', fontsize=10, color=GRAY)
axes[0].set_ylabel('Average Exam Score', fontsize=10, color=GRAY)
axes[0].set_ylim(0, 110)
axes[0].spines['top'].set_visible(False); axes[0].spines['right'].set_visible(False)
axes[1].bar(si_cnt.index, si_cnt.values,
            color=[LIGHT_BLUE, MED_BLUE, BLUE, '#0D2B47'],
            edgecolor='white', width=0.55)
for i, (idx, val) in enumerate(si_cnt.items()):
    axes[1].text(i, val+2, str(val), ha='center', fontsize=11, fontweight='bold', color=GRAY)
axes[1].set_title('Student Count by Study Intensity', fontsize=12, fontweight='bold', color=BLUE)
axes[1].set_xlabel('Study Intensity Group', fontsize=10, color=GRAY)
axes[1].set_ylabel('Number of Students', fontsize=10, color=GRAY)
axes[1].spines['top'].set_visible(False); axes[1].spines['right'].set_visible(False)
plt.suptitle('Study Intensity Analysis', fontsize=13, fontweight='bold', color=BLUE)
plt.tight_layout(); save_fig('chart_study_intensity')

# ── 11. Chart 7 — Pairplot (key variables) ───────────────────────────────────
key_cols = ['study_hours_per_day', 'mental_health_rating',
            'social_media_hours', 'sleep_hours', 'exam_score']
pair_df = df_clean[key_cols + ['score_category']].copy()
pair_df['score_category'] = pair_df['score_category'].astype(str)
g = sns.pairplot(pair_df, hue='score_category',
                 hue_order=['Very Low', 'Low', 'Average', 'High', 'Excellent'],
                 palette=['#C00000','#ED7D31','#FFC000','#2E75B6','#1F4E79'],
                 plot_kws={'alpha': 0.4, 's': 15},
                 diag_kind='hist',
                 vars=key_cols)
g.figure.suptitle('Pairplot — Key Variables by Score Category',
                  fontsize=13, fontweight='bold', color=BLUE, y=1.01)
g.figure.savefig(f'{OUT_VIZ}chart_pairplot.png', dpi=120, bbox_inches='tight')
plt.close()
print("  ✓ Saved: chart_pairplot.png")

print("\n✅ All charts generated successfully!")
print(f"   → Visualizations saved to: {OUT_VIZ}")
print(f"   → Processed data saved to: {OUT_DATA}")
