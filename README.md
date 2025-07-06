# Data-Capstone-Project-2

📊 Netflix Movies & Series Data Analysis

This project is my first step into the world of Data Science and Data Visualization. It involves analyzing a real-world dataset of Netflix content to extract meaningful insights using Python, Pandas, Matplotlib, and Seaborn.

🎯 Goal: To explore trends, discover patterns, and visualize relationships in Netflix's movie and series data such as IMDb scores, genres, languages, runtime, and more.
🔍 Dataset Overview
The dataset used in this project includes:

Title of the content
Genre (some have multiple genres)
IMDb Score
Runtime (in minutes)
Language
Premiere Date
Other metadata like description, country, type, etc.
Dataset Source: Kaggle Netflix Movies and TV Shows Dataset (You can update with actual URL if published)
📌 Key Objectives
Clean and preprocess the dataset
Engineer new insightful features
Visualize genre and rating distributions
Analyze IMDb scores across genres and time
Uncover correlations and patterns
🛠️ Technologies Used
Python 3
Pandas – data manipulation
NumPy – numerical operations
Seaborn & Matplotlib – data visualization
Jupyter Notebook – exploration and plotting
✨ Feature Engineering
Created new columns to support deeper analysis:

Column Name	Description
duration_category	Categorized runtimes into Short, Medium, Long
rating_score	Categorical version of IMDb scores (Poor, Average, Good, Worth Watching)
score_runtime_product	Product of IMDb score × runtime
genre	Exploded into multiple genres from /-separated strings
premiere	Extracted year from premiere date
📈 Key Visualizations
📌 1. Genre Distribution

Countplot of exploded genres to identify most popular categories
📌 2. IMDb Score vs Genre

Strip plot to analyze IMDb scores across genres and languages
Box plot for top 10 most frequent genres to show score spread
📌 3. Rating Score Category

Countplot of rating_score with hue as language
📌 4. Runtime & IMDb Score

Histogram of runtime distribution
Barplot using standard deviation of IMDb score across genres
📌 5. Yearly Trends

Histogram of content premiere years
Line plot showing average IMDb score by premiere year
Linear Regression (lmplot) for IMDb score vs premiere year
📌 6. Correlation Heatmap

Correlation matrix between numeric features like IMDb score, runtime, and their product
📊 Insights Gained
Drama and Documentary genres are most common.
High IMDb scores correlate with slightly longer runtimes.
Several genres show a wide variance in score, indicating subjective reception.
IMDb scores tend to remain fairly consistent across years but show interesting outliers.
🚀 Getting Started
1. Clone this repo

git clone https://github.com/your-username/netflix-data-analysis.git
cd netflix-data-analysis
2. Install required packages

pip install pandas numpy matplotlib seaborn
3. Run the script

python netflix_analysis.py
🧠 Learning Outcomes
Gained hands-on experience with:
Data cleaning and transformation
Data visualization techniques
Feature extraction
Strengthened skills in exploratory data analysis (EDA)
Learned to handle multi-label columns (genre), date/time formatting, and more
