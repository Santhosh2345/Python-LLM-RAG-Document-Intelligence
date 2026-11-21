import os, hashlib

project_path = os.getcwd()
doc_dir = os.path.join(project_path,"data")
all_file = [file_name
    for file_name in os.listdir(doc_dir)
    if file_name.lower().endswith(".pdf")
]

def calculate_file_has(file_path):
    
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
         for block in iter(lambda: file.read(4096), b""):
            sha256.update(block)

    return sha256.hexdigest()

def main():

    for file_name in all_file:
        if os.path.isfile(os.path.join(doc_dir, file_name)):
            file_path = os.path.join(doc_dir, file_name)
            file_hash = calculate_file_has(file_path)

            print(f"File: {os.path.basename(file_path)}")
            print(f'SHA-256: {file_hash}')
        else:
            print(f"{file_name}: PDF file is not exist in {doc_dir}")

if __name__ == "__main__":
    main()