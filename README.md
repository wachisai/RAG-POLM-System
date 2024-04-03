# RAG-POLM-System
RAG system enhances LLMs by adding real-time external knowledge for improved accuracy in business applications. This project demonstrates its implementation with Python, OpenAI, LlamaIndex and MongoDB.

RAG System Implementation Using the POLM Stack
Overview
This repository contains the implementation of a Retrieval-Augmented Generation (RAG) system using the POLM stack (Python, OpenAI, LlamaIndex, and MongoDB). The project is designed to demonstrate how LLMs can be augmented with real-time, relevant data from a secure and updatable non-parametric knowledge source, enhancing their utility in business and productivity applications.

Project Structure

data_preparation/: Scripts for data sourcing and cleaning.

database_setup/: Configuration files and instructions for MongoDB database setup.

embeddings/: Code for generating and managing embeddings.

user_queries/: Implementation of the query engine.

LICENSE: The project's open-source license.

README.md: This file.

Getting Started
Prerequisites

Python 3.8 or later

MongoDB Atlas account

OpenAI API key

Installation

Run install_dependencies.sh to install required Python libraries.

chmod +x install_dependencies.sh
./install_dependencies.sh

Follow the instructions in vector_index_setup.md to configure your MongoDB Atlas vector search index.
Usage

Execute data_sourcing.py to fetch and load the dataset.

python data_preparation/data_sourcing.py

Run data_cleaning.py to clean the dataset.

python data_preparation/data_cleaning.py

Configure the database connection in db_connection.py using your MongoDB URI.

Generate embeddings for your data by running generate_embeddings.py.
python embeddings/generate_embeddings.py

Start querying your RAG system with query_engine.py.
python user_queries/query_engine.py

Data Preparation Scripts
data_sourcing.py: Implement Python code to load the AIatMongoDB/embedded_movies dataset and convert it into a Pandas DataFrame.
data_cleaning.py: Code to clean the DataFrame by removing missing values and unnecessary columns, preparing it for embedding.

Database Setup
db_connection.py: Use PyMongo to connect to your MongoDB Atlas database. Make sure to securely manage your MongoDB URI.
vector_index_setup.md: Provide a markdown guide detailing the steps to create a vector search index in the MongoDB Atlas UI, based on the JSON structure provided in the tutorial.

Embeddings
install_dependencies.sh: Write a bash script to pip install all necessary libraries for the project.
generate_embeddings.py: Include Python code to initialize the OpenAIEmbedding model, generate embeddings for your dataset, and save these embeddings to MongoDB.

User Queries
query_engine.py: Implement the query engine using LlamaIndex, configuring it to handle natural language queries and fetch relevant documents from the MongoDB vector database.

Contributing
Contributions are welcome! Please fork the repository and submit pull requests with your enhancements. 
For major changes, open an issue first to discuss what you would like to change.

License
This project is licensed under the APACHE License - see the LICENSE file for details.
