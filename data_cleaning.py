import pandas as pd

# Load the dataset
dataset_df = pd.read_csv('movies_dataset.csv')

# Remove data points where the plot column is missing
dataset_df = dataset_df.dropna(subset=['plot'])

# Optional: further data cleaning steps can be added here

# Save the cleaned dataset
dataset_df.to_csv('cleaned_movies_dataset.csv', index=False)