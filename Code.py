
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk

from tkinter import ttk

# Load and clean data
df = pd.read_csv("survey_results_public.csv")
columns = ['MainBranch', 'Age', 'Employment', 'RemoteWork', 'EdLevel', 
           'ConvertedCompYearly', 'JobSat', 'Country']
df_clean = df[columns].copy()
df_clean.dropna(subset=['Employment', 'RemoteWork', 'ConvertedCompYearly', 'JobSat'], inplace=True)
df_clean['ConvertedCompYearly'] = pd.to_numeric(df_clean['ConvertedCompYearly'], errors='coerce')
df_clean = df_clean[(df_clean['ConvertedCompYearly'] > 1000) & (df_clean['ConvertedCompYearly'] < 500000)]

# Graph Functions
def show_histogram():
    plt.figure(figsize=(8,5))
    plt.hist(df_clean['ConvertedCompYearly'], bins=40, color='skyblue', edgecolor='black')
    plt.title("Histogram of Yearly Compensation")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

def show_boxplot():
    plt.figure(figsize=(10,6))
    sns.boxplot(data=df_clean, x='Employment', y='ConvertedCompYearly')
    plt.yscale('log')
    plt.title("Box Plot: Salary by Employment Type")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def show_scatter():
    top_countries = df_clean['Country'].value_counts().index[:5]
    df_scatter = df_clean[df_clean['Country'].isin(top_countries)]
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=df_scatter, x='Country', y='ConvertedCompYearly', alpha=0.6)
    plt.title("Scatter Plot: Salary vs Country")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def show_donut():
    remote_counts = df_clean['RemoteWork'].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(remote_counts, labels=remote_counts.index, autopct='%1.1f%%', startangle=140, wedgeprops={'width': 0.4})
    plt.title("Donut Chart: Remote Work Distribution")
    plt.tight_layout()
    plt.show()

def show_bar():
    salary_by_job_sat = df_clean.groupby('JobSat')['ConvertedCompYearly'].mean().sort_values(ascending=False)
    plt.figure(figsize=(10,5))
    salary_by_job_sat.plot(kind='bar', color='orange')
    plt.title("Bar Chart: Avg Salary by Job Satisfaction")
    plt.ylabel("Avg Salary")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def show_heatmap():
    df_corr = df_clean[['ConvertedCompYearly']].copy()
    df_corr['Age_num'] = df_clean['Age'].astype('category').cat.codes
    plt.figure(figsize=(6,4))
    sns.heatmap(df_corr.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

def show_pie():
    ed_counts = df_clean['EdLevel'].value_counts().head(5)
    plt.figure(figsize=(6,6))
    plt.pie(ed_counts, labels=ed_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Pie Chart: Top 5 Education Levels")
    plt.tight_layout()
    plt.show()

def show_horizontal_bar():
    job_sat_counts = df_clean['JobSat'].value_counts().sort_values()
    plt.figure(figsize=(8,5))
    job_sat_counts.plot(kind='barh', color='teal')
    plt.title("Horizontal Bar: Job Satisfaction Levels")
    plt.xlabel("Count")
    plt.tight_layout()
    plt.show()

def show_line_chart():
    age_salary = df_clean.groupby('Age')['ConvertedCompYearly'].mean().dropna()
    plt.figure(figsize=(10,5))
    age_salary.plot(kind='line', marker='o', color='purple')
    plt.title("Line Chart: Avg Salary by Age Group")
    plt.ylabel("Avg Salary")
    plt.xlabel("Age Group")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# GUI Setup
root = tk.Tk()
root.title("Interactive Survey Graphs")
root.geometry("520x500")
root.configure(bg='#e0f7fa')  # Light teal background

# Frame for content
frame = tk.Frame(root, bg='#ffffff', bd=2, relief='groove')
frame.pack(padx=30, pady=30, fill='both', expand=True)

# Title Label
tk.Label(frame, text="Select Graph Type", font=('Arial Rounded MT Bold', 20), bg='#ffffff', fg='#00796b').pack(pady=20)

# ComboBox for Graph Types
options = [
    "Histogram", "Box Plot", "Scatter Plot", "Donut Chart",
    "Bar Chart", "Heatmap", "Pie Chart", "Horizontal Bar", "Line Chart"
]
combo = ttk.Combobox(frame, values=options, font=('Helvetica', 12), width=25, state="readonly")
combo.pack(pady=10)
combo.set("Choose an option")

# Styled Button
generate_btn = tk.Button(frame, text="Generate Graph", font=('Verdana', 12, 'bold'), bg='#00796b', fg='white',
                         activebackground='#004d40', relief='raised',
                         command=lambda: generate_graph(combo.get()))
generate_btn.pack(pady=20)

# Function to generate graph based on choice
def generate_graph(choice):
    if choice == "Histogram":
        show_histogram()
    elif choice == "Box Plot":
        show_boxplot()
    elif choice == "Scatter Plot":
        show_scatter()
    elif choice == "Donut Chart":
        show_donut()
    elif choice == "Bar Chart":
        show_bar()
    elif choice == "Heatmap":
        show_heatmap()
    elif choice == "Pie Chart":
        show_pie()
    elif choice == "Horizontal Bar":
        show_horizontal_bar()
    elif choice == "Line Chart":
        show_line_chart()

# Start the GUI loop
root.mainloop()

