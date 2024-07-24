# Netflix-Data-Analysis-Project

This project aims to perform exploratory data analysis on a Netflix dataset to understand more about movies from the 1990s.

**Netflix**! What started in 1997 as a DVD rental service has since exploded into one of the largest entertainment and media companies.

Given the large number of movies and series available on the platform, it is a perfect opportunity to flex your exploratory data analysis skills and dive into the entertainment industry.

You work for a production company that specializes in nostalgic styles. You want to do some research on movies released in the 1990's. You'll delve into Netflix data and perform exploratory data analysis to better understand this awesome movie decade!

You have been supplied with the dataset `netflix_data.csv`, along with the following table detailing the column names and descriptions. Feel free to experiment further after submitting!

## The data
### **netflix_data.csv**
| Column | Description |
|--------|-------------|
| `show_id` | The ID of the show |
| `type` | Type of show |
| `title` | Title of the show |
| `director` | Director of the show |
| `cast` | Cast of the show |
| `country` | Country of origin |
| `date_added` | Date added to Netflix |
| `release_year` | Year of Netflix release |
| `duration` | Duration of the show in minutes |
| `description` | Description of the show |
| `genre` | Show genre |

## Prerequisites

Ensure you have the following Python libraries installed:

- `pandas`
- `matplotlib`

You can install these libraries using pip:

```sh
pip install pandas matplotlib
```

## Dataset

The dataset file should be named `netflix_data.csv` and located in the same directory as your script.

## Script

Save the following Python script as `netflix_analysis.py`:

```python
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
duration_mode = movies_1990s['duration'].mode()[0]
print(f"\nMost frequent movie duration in the 1990s: {duration_mode} minutes")

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
```

## Running the Script

To execute the script, run the following command in your terminal:

```sh
python netflix_analysis.py
```

## Output

The script will display:

1. First few rows of the dataset.
2. Descriptive statistics for numerical columns.
3. Information about the DataFrame including non-null counts and data types.
4. Most frequent movie duration in the 1990s.
5. Number of short action movies (less than 90 minutes) in the 1990s.
6. Histograms showing:
    - Distribution of movie release years in the 1990s.
    - Distribution of movie durations in the 1990s.
7. Bar plot showing the genre distribution of movies in the 1990s.

## Output Plots
   ![image](https://github.com/user-attachments/assets/ef42c04b-02c6-4593-be4f-c6288c65c2a4)
   ![image](https://github.com/user-attachments/assets/00962566-bf5b-4c25-bf69-c3824f9ae233)
   ![image](https://github.com/user-attachments/assets/b74a28aa-2283-4a36-b3a7-f1ecd0f72ff9)




## Conclusion

This analysis provides insights into the characteristics of Netflix movies from the 1990s, including common movie durations and the prevalence of short action movies. The visualizations offer a clear representation of the data distribution over the decade.

---
