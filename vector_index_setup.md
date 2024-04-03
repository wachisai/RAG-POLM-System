# Vector Index Setup Guide

To set up the vector search index in MongoDB Atlas, follow these steps:

1. Navigate to your MongoDB Atlas dashboard.
2. Select your cluster and then click on 'Collections'.
3. Click on the 'Indexes' tab next to the collections.
4. Choose 'Create Index' and select the 'Vector' index type.
5. Use the following JSON structure for the vector search index:

```json
{
 "fields": [
   {
     "numDimensions": 256,
     "path": "embedding",
     "similarity": "cosine",
     "type": "vector"
   }
 ]
}
```

6. Name your index (e.g., `vector_index`) and save.