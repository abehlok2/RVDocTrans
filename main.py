import PyPDF2
import ocrmypdf
import requests
from bs4 import BeautifulSoup
import os
from langchain.indexes.vectorstore import VectorstoreIndexCreator
from langchain.document_loaders.pdf import PyPDFLoader
from langchain.vectorstores import VectorStore


def ocr_pdfs(input_path: str, output_path: str):
    for filename in os.listdir(input_path):
        if filename.endswith(".pdf"):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, filename)
            ocrmypdf.ocr(input_file, output_file)


def get_pdfs(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    pdf_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.endswith('.pdf'):
            pdf_links.append(href)

    for pdf_link in pdf_links:
        response = requests.get(pdf_link)
        filename = os.path.basename(pdf_link)
        with open(filename, 'wb') as file:
            file.write(response.content)


def get_text_as_str(pdf_path: str, vectorstore: VectorStore):
    pdf_loader = PyPDFLoader(pdf_path)
    vectorstore = VectorstoreIndexCreator.from_loaders(loaders=[pdf_loader])


def main():
    pdf_loader = PyPDFLoader()
    vectorstore = VectorstoreIndexCreator.from_loaders(loaders=[])

    return


if __name__ == '__main__':
    main()
