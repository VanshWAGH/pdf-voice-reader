import subprocess
from PyPDF2 import PdfReader
#library needed to read the pdfs


def speak_text(text):
    #here I have used espeak command since I am in my Ubuntu machine this command name may vary for windows or mac
    command = f'espeak "{text}"'
    subprocess.run(command, shell=True)


def read_pdf(pdf_file):
    try:
        with open(pdf_file, 'rb') as file: #opening the file
            reader = PdfReader(file) #storing the contents in reader
            for page_number, page in enumerate(reader.pages):
                text = page.extract_text() #abstracted pages
                speak_text(text) #speak function

    except FileNotFoundError:
        print(f"Error: PDF file '{pdf_file}' not found.")


def main():
    pdf_file = 'test.pdf'

    read_pdf(pdf_file)


if __name__ == '__main__':
    main()
