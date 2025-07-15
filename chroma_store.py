import chromadb
from chromadb.utils import embedding_functions

def store_versions():
    print("Initializing ChromaDB client...")
    client = chromadb.Client()

    print("Creating collection: book_versions")
    collection = client.create_collection(name="book_versions")

    embedder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

    print("Storing all versions with metadata...")
    versions = [
        ("chapter1.txt", "original"),
        ("chapter1_ai.txt", "ai_writer"),
        ("chapter1_reviewed.txt", "ai_reviewer"),
        ("chapter1_final.txt", "human_final"),
    ]

    for i, (file, version_name) in enumerate(versions):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        collection.add(
            documents=[content],
            ids=[f"doc_{i}"],
            metadatas=[{"version": version_name}]
        )
        print(f"Stored: {version_name}")

    print("All versions stored in ChromaDB.")

def search_versions(query_text):
    print(f"\nSearching for: {query_text}")
    client = chromadb.Client()
    collection = client.get_collection(name="book_versions")

    results = collection.query(
        query_texts=[query_text],
        n_results=2
    )

    print("\nTop Matching Results:\n")
    for result, metadata in zip(results["documents"][0], results["metadatas"][0]):
        print(f"Version: {metadata['version']}")
        print(result[:300], "...\n")

if __name__ == "__main__":
    store_versions()

    search_versions("What is the main theme of the chapter?")
