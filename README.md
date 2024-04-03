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
Clone the repository to your local machine.
Run install_dependencies.sh to install required Python libraries.
bash
Copy code
chmod +x install_dependencies.sh
./install_dependencies.sh
Follow the instructions in vector_index_setup.md to configure your MongoDB Atlas vector search index.
Usage
Execute data_sourcing.py to fetch and load the dataset.
bash
Copy code
python data_preparation/data_sourcing.py
Run data_cleaning.py to clean the dataset.
bash
Copy code
python data_preparation/data_cleaning.py
Configure the database connection in db_connection.py using your MongoDB URI.
Generate embeddings for your data by running generate_embeddings.py.
bash
Copy code
python embeddings/generate_embeddings.py
Start querying your RAG system with query_engine.py.
bash
Copy code
python user_queries/query_engine.py
Contributing
Contributions are welcome! Please fork the repository and submit pull requests with your enhancements. For major changes, open an issue first to discuss what you would like to change.

License
This project is licensed under the APACHE License - see the LICENSE file for details.
