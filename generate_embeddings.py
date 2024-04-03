from llama_index.embeddings.openai import OpenAIEmbedding

# Assuming you have already loaded your data and it's ready for embedding
# This is just a placeholder for the actual embedding generation code
def generate_embeddings(data):
    embed_model = OpenAIEmbedding(model="text-embedding-3-small", dimensions=256)
    embeddings = embed_model.get_text_embedding(data)
    return embeddings