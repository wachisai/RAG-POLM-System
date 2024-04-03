from datasets import load_dataset
import pandas as pd

# Load the dataset from Hugging Face
dataset = load_dataset("AIatMongoDB/embedded_movies")

# Convert the dataset to a pandas dataframe
dataset_df = pd.DataFrame(dataset['train'])

# Save the dataframe to a CSV for further use
dataset_df.to_csv('movies_dataset.csv', index=False)