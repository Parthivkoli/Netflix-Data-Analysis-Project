# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Display the first few rows of the DataFrame to understand its structure
print("First few rows of the dataset:")
print(netflix_df.head())

# Descriptive statistics for numerical columns
print("\nDescriptive statistics for numerical columns:")
print(netflix_df.describe())

# Information about the DataFrame including non-null counts and data types
print("\nInformation about the DataFrame:")
print(netflix_df.info())

# Filter movies from the 1990s
movies_1990s = netflix_df[(netflix_df['type'] == 'Movie') & 
                          (netflix_df['release_year'] >= 1990) & 
                          (netflix_df['release_year'] < 2000)]

# Find the most frequent movie duration in the 1990s
duration = movies_1990s['duration'].mode()[0]
print(f"\nMost frequent movie duration in the 1990s: {duration} minutes")

# Filter to find short action movies from the 1990s
short_action_movies_1990s = movies_1990s[(movies_1990s['duration'] < 90) & 
                                         (movies_1990s['genre'] == 'Action')]

# Count the number of short action movies
short_movie_count = short_action_movies_1990s.shape[0]
print(f"Number of short action movies (less than 90 minutes) in the 1990s: {short_movie_count}")

# Plot the distribution of release years in the 1990s
plt.figure(figsize=(10, 6))
movies_1990s['release_year'].hist(bins=range(1990, 2001), edgecolor='black')
plt.title('Distribution of Movie Release Years in the 1990s')
plt.xlabel('Release Year')
plt.ylabel('Number of Movies')
plt.grid(False)
plt.show()

# Plot the distribution of movie durations in the 1990s
plt.figure(figsize=(10, 6))
movies_1990s['duration'].hist(bins=30, edgecolor='black')
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.grid(False)
plt.show()

# Plot the distribution of genres for movies in the 1990s
plt.figure(figsize=(12, 6))
movies_1990s['genre'].value_counts().plot(kind='bar')
plt.title('Genre Distribution of Movies in the 1990s')
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.xticks(rotation=45, ha='right')
plt.show()
