from pipelines import pipeline
import docx


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


f = getText("C:/Users/Sagnik/Desktop/The_text_files/test.docx")

print(f)
nlp = pipeline("question-generation")

import time

start_time = time.time()
anser = nlp(f)
print(anser)
end = time.time()
print("--- %s seconds ---" % (end - start_time))
