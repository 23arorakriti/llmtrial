import requests
from bs4 import BeautifulSoup
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
import os
import requests
from PyPDF2 import PdfReader

os.environ['HUGGINGFACE_TOKEN'] = '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'


repo_id = "mistralai/Mistral-Nemo-Instruct-2407"
llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.5,
    max_length=128
)


def webpage_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all('p')
        text = "\n".join([para.get_text() for para in paragraphs])
        return text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""

def getpdftext(pdf):
    text = ""
    pdfreader = PdfReader(pdf)
    for page in pdfreader.pages:
        text += page.extract_text() or ""
    return text

def combined_text(urls, pdfpath):
    combinedtext = ""
    for pdf in pdfpath:
        print(f"Extracting text from {pdf}")
        combinedtext += f"PDF: {pdf}\n"
        combinedtext += getpdftext(pdf) + "\n"
    for url in urls:
        print(f"Fetching text from {url}")
        combinedtext += f"URL: {url}\n"
        combinedtext += webpage_text(url) + "\n\n"
    return combinedtext

def splitting(text, chunksize):
    chunks = []
    length = len(text)
    for i in range(0, length, chunksize):
        chunk = text[i:i+chunksize]
        chunks.append(chunk)
    return chunks

pdfpath = ["auto.pdf","Preventing-autoimmunity.pdf"]
urls = [
    "https://www.elcaminohealth.org/stay-healthy/blog/truth-about-autoimmune-disease",
    "https://www.kelsey-seybold.com/your-health-resources/blog/debunking-myths-about-lupus",
    
]


text = combined_text(urls,pdfpath)


chunksize = 2000
chunks = splitting(text, chunksize)


print("Combining text from URLs and PDFs.")
text = combined_text(urls, pdfpath)
prompt = PromptTemplate(
    template="Summarize the following text in detail and depth with all important points in bullet points:\n\n{input_text}\n\nSummary:",
    input_variables=["input_text"]
)

chain = (prompt | llm)


summaries = []
for chunk in chunks:

        response = chain.invoke({"input_text": chunk})
        summaries.append(response)
    

final_summary = " ".join(summaries)
print("Summary:\n", final_summary)

#  file path 
file_path = "autoimmune_summary.txt"  
with open(file_path, "w",encoding='utf-8') as file:
    file.write(final_summary)

print(f"Summary saved to {file_path}")

