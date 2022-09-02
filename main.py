import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# As a part of "2022 Python for Machine Learning & Data Science Masterclass" by Pierian Training, this Data Analysis
# attempts to clarify the relationship of critic sites (Rotten Tomatoes, IMDB, Metacritic), and critic sites that also
# sell tickets to movies (Fandango), regarding their ratings. Datasource provided in course, from 2015.
# https://www.udemy.com/course/python-for-machine-learning-data-science-masterclass/

# Problem: Do critic sites, that sell movie tickets tend to rate movies higher, to sell more tickets?

# Part 1. Fandango Analysis.

# Reading in Fandango Datasource.
fandango = pd.read_csv('fandango_scrape.csv')

# Displaying data structure.
print("Fandango data structure: \n\n", fandango.head(), "\n")

# Basic plot between User ratings and Fandango ratings.
plt.figure(figsize=(10, 4), dpi=150)
sns.scatterplot(data=fandango, y='VOTES', x='RATING')
plt.title("User votes vs. Fandango ratings")
plt.show()

# Correlation between columns.
print("Fandango correlation between columns: \n\n", fandango.corr(), "\n")

# Extracting YEAR from movie titles to new column.
fandango['YEAR'] = fandango['FILM'].apply(lambda title: title.split('(')[-1].replace(')', ''))

# Displaying DataFrame, number of movies by year.
print("Fandango movies by year: \n\n", fandango['YEAR'].value_counts(), "\n")

# Visualizing number of movies by year.
sns.countplot(data=fandango, x='YEAR')
plt.title("Movies per year")
plt.show()

# Top 10 movies by number of User votes.
print("Top 10 movies by number of User votes: \n\n", fandango.nlargest(10, 'VOTES'), "\n")

# Counting how many movies have 0 votes from Users.
print((fandango['VOTES'] == 0).sum())
# Another way, without using .sum()
# print(len(fandango[fandango['VOTES'] == 0]))

# Creating DataFrame for only User reviewed movies.
fan_reviewed = fandango[fandango['VOTES'] > 0]

# Double KDEPlot on the same figure, for easier visualisation between User ratings and Fandango Stars.
plt.figure(figsize=(8, 4), dpi=150)
sns.kdeplot(data=fan_reviewed, x='RATING', clip=[0, 5], fill=True, label='User (True) Rating')
sns.kdeplot(data=fan_reviewed, x='STARS', clip=[0, 5], fill=True, label='Fandango Stars Displayed')
plt.legend(loc=(0.02, 0.8))
plt.title("User rating vs. Fandango ratings")
plt.show()

# Creating column, to see if the Fandango Star rating differs from User ratings, and if yes, by how much.
fan_reviewed['STARS_DIFF'] = (fan_reviewed['STARS'] - fan_reviewed['RATING']).round(2)

# Visualizing difference with count plot.
sns.countplot(data=fan_reviewed, x='STARS_DIFF')
plt.title("Difference in Fandango ratings by number of stars")
plt.show()

# Previous results show, that there is one movie, that has 1 whole star discrepancy.
print(fan_reviewed[fan_reviewed['STARS_DIFF'] == 1])

# Part 2. IMDB, Metacritic, Rotten Tomatoes analysis.

# Reading in Datasource.
other_sites = pd.read_csv('all_sites_scores.csv')

# Displaying data structure.
print(other_sites.head())

# Visualizing other sites' scoring, keeping in mind, that some of them use a 0-100 system, rather than 0-5.
plt.figure(figsize=(10, 6), dpi=150)
sns.scatterplot(data=other_sites, x='RottenTomatoes', y='RottenTomatoes_User')
plt.ylim(0, 100)
plt.xlim(0, 100)
plt.title("Rotten Tomatoes Scores vs. Rotten Tomatoes User Ratings")
plt.show()
# Only a couple movies show outlying difference in scoring between Users and Rotten Tomatoes critics.

# Taking Rotten Tomatoes' reviews as base, and creating its own column, as it seems to be the most consistent.
other_sites['Rotten_Diff'] = other_sites['RottenTomatoes'] - other_sites['RottenTomatoes_User']

plt.figure(figsize=(10, 4), dpi=150)
# Visualizing Rotten Tomatoes' Critics' and User review discrepancy.
sns.histplot(data=other_sites, x='Rotten_Diff', kde=True, bins=25)
plt.title("Difference between Rotten Tomatoes vs. User Ratings")
plt.show()

# Taking the absolute value of the new column, to see only the absolute differences.
sns.histplot(x=other_sites['Rotten_Diff'].apply(abs), kde=True, bins=25)
plt.title("Absolute difference between Rotten Tomatoes vs. User Ratings")
plt.show()

# Smallest difference movies by Rotten Tomatoes reviews.
print(other_sites.nsmallest(5, 'Rotten_Diff')['FILM'])
# Largest difference movies by Rotten Tomatoes reviews.
print(other_sites.nlargest(5, 'Rotten_Diff')['FILM'])

# Visualizing Metacritic scores, keeping in mind, that Metacritic uses a 0-100 scoring system.
plt.figure(figsize=(10, 4), dpi=150)
sns.scatterplot(data=other_sites, x='Metacritic', y='Metacritic_User')
plt.ylim(0, 10)
plt.xlim(0, 100)
plt.title("Metacritic Scores vs. Metacritic User Ratings")
plt.show()

# Visualizing Metacritic User review counts vs. IMDB User review counts.
plt.figure(figsize=(10, 4), dpi=150)
sns.scatterplot(data=other_sites, x='Metacritic_user_vote_count', y='IMDB_user_vote_count')
plt.title("Metacritic User vote count vs. IMDB User vote count")
plt.show()

# Highest IMDB User voted movie.
print(other_sites.nlargest(1, 'IMDB_user_vote_count'))
# Highest Metacritic User voted movie.
print(other_sites.nlargest(1, 'Metacritic_user_vote_count'))

# Part 3. Comparing the results of the 2 Datasources.

# Inner merge to a new DataFrame, to only see movies which have been reviewed by Fandango Users across the sites.
df = pd.merge(fandango, other_sites, on='FILM', how='inner')

# Normalizing the scores to 0-5 ratings with 1 decimal accuracy.
df['RT_Norm'] = np.round(df['RottenTomatoes'] / 20, 1)
df['RT_U_Norm'] = np.round(df['RottenTomatoes_User'] / 20, 1)
df['Meta_Norm'] = np.round(df['Metacritic'] / 20, 1)
df['Meta_U_Norm'] = np.round(df['Metacritic_User'] / 2, 1)
df['IMDB_Norm'] = np.round(df['IMDB'] / 2, 1)

# New DataFrame with the normalized scores across all platforms.
norm_scores = df[['STARS', 'RATING', 'RT_Norm', 'RT_U_Norm', 'Meta_Norm', 'Meta_U_Norm', 'IMDB_Norm']]

# Displaying the new DataFrame.
print(norm_scores.head())

# Visualizing the normalized values across the sites --> Clipping results, to not have scores below 0 and above 5.
fig, ax = plt.subplots()
sns.kdeplot(data=norm_scores, clip=[0, 5], shade=True, palette="Set1")
sns.move_legend(ax, "upper left")
plt.title("Normalized Scores over all sites")
plt.show()

# Grabbing Rotten Tomatoes vs Fandango Critic Scores from previous plot.
# Re-declaring fig,ax to be able to move the legend on this plot.
fig, ax = plt.subplots()
sns.kdeplot(data=norm_scores[['RT_Norm', 'STARS']], clip=[0, 5], shade=True, palette="Set1")
sns.move_legend(ax, "upper left")
plt.title("Rotten Tomatoes vs. Fandango Scores (Same Movies)")
plt.show()

# Quantifying the scores over all sites.
sns.histplot(data=norm_scores, bins=25, palette="Set1")
sns.move_legend(ax, "upper left")
plt.title("Quantified Normalized Scores over all sites")
plt.show()

# Visualizing tilt in scores on cluster map.
sns.clustermap(norm_scores, cmap='magma', col_cluster=False)
plt.show()
# Cluster map shows a clear tilt in Fandango Scores as well as User Ratings.

# Final DataFrame for conclusion.
norm_films = df[['FILM', 'STARS', 'RATING',
                 'RT_Norm', 'RT_U_Norm', 'Meta_Norm', 'Meta_U_Norm', 'IMDB_Norm']]

# Top 10 Worst films based on Rotten Tomatoes Scoring.
worst_films = norm_films.nsmallest(10, 'RT_Norm')

# Visualizing the Top 10 Worst films across all sites, based on Rotten Tomatoes Scoring.
sns.kdeplot(data=worst_films, clip=[0, 5], shade=True, palette="Set1")
plt.title("Top 10 Worst Movies' ratings across all sites")
plt.show()

# Quantifying the Top 10 Worst films' scores.
plt.figure(figsize=(12, 6))
sns.histplot(data=worst_films, bins=25, palette="Set1")
plt.title("Number of Top 10 Worst Movies")
sns.move_legend(ax, "upper right")
plt.show()

# Conclusion: sites that sell movie tickets (Fandango in this case study), tend to rate movies higher.
