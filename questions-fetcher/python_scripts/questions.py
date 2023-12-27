import docx
import re

def extract_questions_and_options(file_path):
    doc = docx.Document(file_path)
    questions_and_options = []
    question_pattern = re.compile(r"\(?\d+[.)]+[.]?\s*(.*?)(?=\s*[A-D]+[.\)]|$)")
    option_pattern = re.compile(
        r"[A-D]+[.)]+[.]?\s*(.*?)(?=\s*[A-D][\.\)]|$|\s*\([A-D])")

    current_question = None

    for para in doc.paragraphs:
        question_matches = question_pattern.findall(para.text.strip())
        option_matches = option_pattern.findall(para.text.strip())

        if question_matches:
            if current_question:
                questions_and_options.append(current_question)

            current_question = {'question': question_matches[0], 'options': []}
        elif option_matches and current_question:
            current_question['options'].extend(option_matches)

    if current_question:
        questions_and_options.append(current_question)

    return questions_and_options

if __name__ == "__main__":
    file_path = "../data/test2.docx"
    questions_and_options = extract_questions_and_options(file_path)

    for i, qa_pair in enumerate(questions_and_options, 1):
        print(f"Question {i}: {qa_pair['question']}")
        for j, option in enumerate(qa_pair['options'], 1):
            print(f"Option {j}: {option}")
