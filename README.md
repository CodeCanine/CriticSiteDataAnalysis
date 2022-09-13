# CriticSiteDataAnalysis

As a part of <i>"2022 Python for Machine Learning & Data Science Masterclass"</i> by <i>Pierian Training</i>, this Data Analysis
attempts to clarify the relationship between critic sites (Rotten Tomatoes, IMDB, Metacritic), and critic sites that sell tickets to
movies (Fandango), regarding their ratings. Datasource provided in course, from 2015.

https://www.udemy.com/course/python-for-machine-learning-data-science-masterclass/

<b>Task:</b>
Find out if Fandango, that reviews movies as well as sells movie tickets, tend to rate films higher, to sell more tickets, or not.

<b>Approach:</b>
- Datafiles provided by course in .csv form
- Data requires modification to be able to create accurate plots
- Create multiple plots
- Analyze the plots
- Make a conclusion

<b>Plots:</b>
# 1 Plot between User ratings and Fandango ratings:
Most of the User ratings and Fandango stars both tend to take place between **3-4.5**. Scores seem to be tilted.
![scatter](https://user-images.githubusercontent.com/9075212/189904457-deed4869-f485-49ed-b216-4800c8b1a40c.png)

# 2 Plot to visualize the number of movies by year:
![count](https://user-images.githubusercontent.com/9075212/189904431-521247e5-1808-4abc-86b0-9d45274096de.png)

# 3 Double KDEPlot on the same figure, for easier visualisation between User ratings and Fandango Stars:
Density of User ratings and Fandango stars are the highest at **4** stars. Scores seem to be tilted clearer.
![kde](https://user-images.githubusercontent.com/9075212/189904447-f1c0cf47-4fd0-4807-93ea-8d736903e8d0.png)

# 4 Plot to Visualize difference between User ratings and Fandango ratings:
Fandango rounds scores by 0.5. This visualisation shows, how many movies tend to be affected by this rounding.
![count_2](https://user-images.githubusercontent.com/9075212/189904435-07d33fd8-ca45-4d08-bc26-6b4599d3a2dc.png)

# 5 Visualizing Rotten Tomatoes' ratings (keeping in mind, that they use a 0-100 system, rather than 0-5.):
Rotten Tomatoes has an even distribution for User movie ratings, and RT movie scores.
![scatter_2](https://user-images.githubusercontent.com/9075212/189904458-6d4887cc-a3ff-4856-b1a1-9593cf90100e.png)

# 6 Visualizing Rotten Tomatoes Critics' and User reviews discrepancy:
Difference can also be negative between Critic and User ratings, however the highest density is at 0. Seems to be a reliable source.
![hist](https://user-images.githubusercontent.com/9075212/189904436-f87aad95-06f0-4363-b64c-4169d9f3c1bc.png)

# 7 Taking the absolute value of the new column, to see only the absolute differences:
Further refinging the plot, showing us, that there are clear differences, but not too many, with no gaps as in Fandango's case.
![hist_2](https://user-images.githubusercontent.com/9075212/189904437-b4fba9df-5ad5-4b02-817e-32069257adf1.png)

# 8 Visualizing Metacritic scores (keeping in mind, that Metacritic uses a 0-100 scoring system):
Metacritic has an even distribution for User movie ratings, and Metacritic movie scores, however maybe a bit too short on the low end.
![scatter_3](https://user-images.githubusercontent.com/9075212/189904459-5d3945d7-6008-42e9-957f-c52ef2ceca7b.png)

# 9 Visualizing Metacritic User review counts vs. IMDB User review counts:
IMDB has a much higher userbase than Metacritic.
![scatter_4](https://user-images.githubusercontent.com/9075212/189904462-94fefd31-1b82-47c0-b965-2ca4e51e3115.png)

# 10 Visualizing the normalized values across the sites --> Clipping results, to not have scores below 0 and above 5:
Fandango Stars are the most tilted between all the onsidered sites, with their Users the most biased towards giving good scores.
Rotten Tomatoes seem to be the most consistent still.
![kde_2](https://user-images.githubusercontent.com/9075212/189904450-f6d494ff-f837-4b50-a05a-80694c25dfb0.png)

# 11 Rotten Tomatoes vs. Fandango Scores (Same Movies):
RT still show clear distribution over the same reviewed movies, while Fandango has enormously higher opinion on them.
![kde_3](https://user-images.githubusercontent.com/9075212/189904452-99d76fa6-85ef-4e2b-b4eb-c3d174e11566.png)

# 12 Quantifying the scores/movies over all sites:
![hist_3](https://user-images.githubusercontent.com/9075212/189904440-307110a7-f5d3-48a8-98db-049f3e75ed7b.png)

# 13 Visualizing tilt in scores on cluster map.
![cluster](https://user-images.githubusercontent.com/9075212/189904426-df9e92d2-5d1c-416d-990c-5d76a7849556.png)

# 14 Visualizing the Top 10 Worst films across all sites, based on Rotten Tomatoes Scoring: 
![kde_4](https://user-images.githubusercontent.com/9075212/189904455-fa0e3744-160f-45b5-a3d1-b32eeddb9a8c.png)

# 15 Quantifying the Top 10 Worst films' scores
For the Top 10 worst movies Fandango's rating tend to be around 3,5 Stars, while Rotten Tomatoes is between 0 - 1.
![hist_4](https://user-images.githubusercontent.com/9075212/189904444-77c537d2-8189-439e-84fa-59ab3ba09e87.png)

<b>Conclusion:</b>

Based on this study Fandango in this case study, tend to rate movies higher, to sell more tickets.
Last words:

This analysis was based on a 2015 dataset, provided by the author of the course, and does not represent any of the sites' current or past real world
usage nor represent real values.
