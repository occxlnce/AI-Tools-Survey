import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the CSV file into a pandas DataFrame
df = pd.read_csv('surveyForm.csv')

# Step 2: Data Analysis and Visualization

# Question 1: How often do you use AI tools?
usage_counts = df['usage'].value_counts()
plt.figure(figsize=(8, 6))
usage_counts.plot(kind='bar', color='skyblue')
plt.title('Frequency of AI Tool Usage')
plt.xlabel('Usage Frequency')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('usage_frequency.png')
plt.show()

# Question 2: Impact of AI tools on academic performance
plt.figure(figsize=(8, 6))
plt.hist(df['impact'], bins=5, color='lightgreen', edgecolor='black')
plt.title('Impact of AI Tools on Academic Performance')
plt.xlabel('Impact Rating')
plt.ylabel('Number of Students')
plt.xticks(range(1, 6))
plt.tight_layout()
plt.savefig('impact_histogram.png')
plt.show()

# Question 3: Marks range since using AI tools
marks_range_counts = df['marks_range'].value_counts()
plt.figure(figsize=(8, 6))
marks_range_counts.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'])
plt.title('Distribution of Marks Range')
plt.ylabel('')
plt.tight_layout()
plt.savefig('marks_range_pie.png')
plt.show()

# Question 4: Hours per week using AI tools
hours_per_week_counts = df['hours_per_week'].value_counts().sort_index()
plt.figure(figsize=(8, 6))
hours_per_week_counts.plot(kind='line', marker='o', color='orange')
plt.title('Weekly Hours Spent Using AI Tools')
plt.xlabel('Hours per Week')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('hours_per_week_line.png')
plt.show()

# Question 5: Benefits of AI tools for research activities
plt.figure(figsize=(8, 6))
plt.hist(df['benefit'], bins=5, color='lightblue', edgecolor='black')
plt.title('Perceived Benefits of AI Tools for Research')
plt.xlabel('Benefit Rating')
plt.ylabel('Number of Students')
plt.xticks(range(1, 6))
plt.tight_layout()
plt.savefig('benefit_histogram.png')
plt.show()

# Question 6: Challenging technical issues when using AI tools
plt.figure(figsize=(8, 6))
plt.hist(df['challenging'], bins=5, color='lightpink', edgecolor='black')
plt.title('Perceived Challenges of AI Tools')
plt.xlabel('Challenge Rating')
plt.ylabel('Number of Students')
plt.xticks(range(1, 6))
plt.tight_layout()
plt.savefig('challenging_histogram.png')
plt.show()

# Question 7: Grade improvement since using AI tools
grade_improvement_counts = df['grade_improvement'].value_counts()
plt.figure(figsize=(8, 6))
grade_improvement_counts.plot(kind='bar', color='lightgreen')
plt.title('Grade Improvement Since Using AI Tools')
plt.xlabel('Grade Improvement Range')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grade_improvement_bar.png')
plt.show()
