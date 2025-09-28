import argparse
import os
from llama_index import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
from dotenv import load_dotenv

load_dotenv()
INDEX_DIR = "data/index"

def build_index():
    docs = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(docs)
    index.storage_context.persist(persist_dir=INDEX_DIR)
    return index

def query_index(query: str):
    if not os.path.exists(INDEX_DIR):
        raise ValueError("Index not built. Run build_index first.")
    storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return str(response)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", action="store_true")
    parser.add_argument("--query", type=str)
    args = parser.parse_args()

    if args.build:
        build_index()
        print("Index built and saved.")
    elif args.query:
        print(query_index(args.query))
