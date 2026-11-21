import chromadb
import chunk

chromadb_name = "7_different_topics"
client = chromadb.PersistentClient(path="./chromadb")
collection = client.create_collection(chromadb_name)

def store_chunks_in_chormadb(all_chunks):
    collection.upsert(
        ids= [f'chunk_{i}' for i in range(0, len(all_chunks))],
        documents= [chunk["text"] for chunk in all_chunks],
        metadatas= [{"source":chunk["source"]} for chunk in all_chunks]
    )
    stored_data = collection.get()
    for i in range(len(stored_data["ids"])):
        print(f'\nID: {stored_data["ids"][i]+1}')
        print(f'\nDocuments: {stored_data["documents"][i]}')
        print(f'\nMetadata: {stored_data["metadatas"][i]}')

def main():
    all_chunks = chunk.all_chunks
    store_chunks_in_chormadb(all_chunks)