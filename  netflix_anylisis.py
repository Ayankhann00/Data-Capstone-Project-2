import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('netflix.csv')

# Convert 'premiere' to datetime
df['premiere'] = pd.to_datetime(df['premiere'])

# Extract year from premiere
df['premiere'] = df['premiere'].dt.year

# Drop 'year' column if exists
if 'year' in df.columns:
    df.drop(['year'], axis=1, inplace=True)

# Categorize duration
df['duration_category'] = df['runtime'].apply(
    lambda x: 'Short' if x < 80 else 'Medium' if x <= 100 else 'Long'
)

# Categorize rating_score
df['rating_score'] = df['imdb_score'].apply(
    lambda x: 'Average' if x == 6.0 else 'Poor' if x < 6.0 else 'Good' if x < 8.0 else 'Worth Watching'
)

# Create score-runtime product
df['score_runtime_product'] = df['imdb_score'] * df['runtime']

# Drop missing values
df.dropna(inplace=True)

# Split and explode genres
df['genre'] = df['genre'].str.split('/')
df = df.explode('genre').reset_index(drop=True)
df['genre'] = df['genre'].astype('category')

# Set seaborn style
sns.set_style('darkgrid')

# Plot genre distribution
g = sns.catplot(
    y='genre', data=df, kind='count',
    order=df['genre'].value_counts().index,
    height=13, aspect=0.5, color='purple'
)
g.set_axis_labels("Count", "Genre")
plt.title("Distribution of Music Genres", pad=20)
plt.tight_layout()
plt.show()

# Stripplot of imdb_score by genre and language
plt.figure(figsize=(10, 16))
sns.stripplot(
    x='imdb_score', y='genre', data=df,
    hue='language', palette='coolwarm',
    jitter=True, alpha=0.6
)
plt.xlabel("IMDb Score")
plt.ylabel("Genre")
plt.title("Distribution of IMDb Scores by Genre and Language", pad=20)
plt.xticks(rotation=45, ha='right')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='magma', linewidths=0.5, linecolor='black')
plt.title('Correlation Heatmap of Netflix Dataset')
plt.tight_layout()
plt.show()

# Histogram of runtime
sns.histplot(df['runtime'], kde=True, bins=30)
plt.title("Runtime Distribution")
plt.tight_layout()
plt.show()

# Barplot: IMDb Score Std by Genre and Duration
plt.figure(figsize=(14, 12))
sns.barplot(
    y='genre', x='imdb_score', data=df,
    hue='duration_category', estimator=np.std,
    palette='coolwarm'
)
plt.title('Standard Deviation of IMDb Scores by Genre and Duration Category', fontsize=19)
plt.xlabel('IMDb Score (Standard Deviation)')
plt.ylabel('Genre')
plt.legend(title='Category', loc='upper right')
plt.tight_layout()
plt.show()

# Linear Regression plot: IMDb vs Premiere
sns.lmplot(
    x='premiere', y='imdb_score', data=df,
    aspect=1.5, height=6,
    line_kws={'color': 'red'},
    scatter_kws={'alpha': 0.5}
)
plt.title("Linear Regression: IMDb Score vs Premiere Year", fontsize=14)
plt.xlabel("Premiere Year")
plt.ylabel("IMDb Score")
plt.tight_layout()
plt.show()

# Premiere year distribution
df['premiere'].hist()
plt.title('Release Year Distribution')
plt.xlabel('Premiere Year')
plt.tight_layout()
plt.show()

# Plot avg IMDb score over years
df.groupby('premiere')['imdb_score'].mean().plot()
plt.title("Average IMDb Score Over Years")
plt.ylabel("IMDb Score")
plt.xlabel("Premiere Year")
plt.tight_layout()
plt.grid(True)
plt.show()

# Boxplot: Top 10 genres
top_genres = df['genre'].value_counts().nlargest(10).index
filtered_df = df[df['genre'].isin(top_genres)]

plt.figure(figsize=(17, 13))
sns.boxplot(
    y='genre', x='imdb_score',
    data=filtered_df, palette='viridis'
)
plt.title('IMDb Score Distribution for Top 10 Genres')
plt.xlabel('IMDb Score')
plt.ylabel('Genre')
plt.tight_layout()
plt.show()
