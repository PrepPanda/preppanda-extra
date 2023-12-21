import PyPDF2
import re


def extract_question_answers(pdf_path):
    questions = []
    options = []

    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            question_pattern = re.compile(r"\d+\.\s(.*?)(?=(\d+\.|$))", re.DOTALL)
            option_pattern = re.compile(r"[A-E]\.\s(.*?)(?=[A-E]\.|\Z)", re.DOTALL)

            questions.extend(question_pattern.findall(text))
            options.extend(option_pattern.findall(text))

    return questions, options


pdf_path = "data/pdfs/test.pdf"
quesitons, options = extract_question_answers(pdf_path=pdf_path)

for i in range(len(quesitons)):
    print(f"Question {i+1}: {quesitons[i]}")
    print(f"Options: {options[i]}")
