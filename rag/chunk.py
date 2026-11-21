from pypdf import PdfReader
import os, json
import logging

# Checking the dir and file existence and read the extracting the pdf
project_path = os.getcwd()
log_filename = "rag_log.txt"

log_dir = os.path.join(project_path, "logs")
log_file = os.path.join(log_dir, log_filename)
logger = logging.getLogger(__name__)
all_chunks = []

def main():
    if os.path.exists(log_dir):
        print(f'Log directory is exist: {log_dir}')
    else:
        os.mkdir(log_dir)

    if os.path.isfile(log_file):
        logging.basicConfig(filemode="a", level=logging.DEBUG, filename=log_file, format= "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    else:
        with open(log_file, "w"):
            logging.basicConfig(filemode="w", level=logging.DEBUG, filename=log_file, format= "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    doc_path = os.path.join(project_path,"data")
    all_documents = []
    pdf_text = ""

    if os.path.exists(doc_path):
        all_documents = [ file
            for file in os.listdir(doc_path)
            if file.lower().endswith(".pdf")
        ]

        for doc in all_documents:
            reader = PdfReader(os.path.join(doc_path,doc))
            pdf_text = "\n\n".join(page.extract_text() or " " for page in reader.pages)

            chunks = chunk_by_length_overlap(pdf_text)
            for chunk in chunks:
                all_chunks.append({
                    "source": doc,
                    "text": chunk
                })

        logger.info("File successfully readed")
    else:
        logger.error("Document directors are not existing")

def chunk_by_length_overlap(pdf_text, chunk_size = 50, steprate=40):
    chunks = []
    for i in range(0, len(pdf_text), steprate):
        chunks.append( pdf_text[i:chunk_size + i])
    return chunks

if __name__ == "__main__":
    main()
