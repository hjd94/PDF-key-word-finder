import nltk
import os 
import PyPDF2
import pandas

# ___________________________________
# nltk.download('punkt')
# ___________________________________


folder_path = r""
Key_words = ["", ""]
output_name = ""

sentences_list = []
empty_pages = set()
file_names = os.listdir(folder_path)
file_names = [file_name for file_name in file_names if file_name.endswith(".pdf")]
for file_name in file_names:
    pdf_submission = PyPDF2.PdfReader(os.join(folder_path, file_name))
    for page in pdf_submission.pages:
        page_text = page.extractText()
        tokenize_sentence = nltk.tokenize.sent_tokenize(page_text)
        if len(tokenize_sentence) == 0:
            empty_pages = empty_pages.union({file_name})
        sentences = [[file_name, sentence] for sentence in tokenize_sentence if any(word in sentence for word in Key_words)]
        sentences_list.extend(sentences)

print(f"Number of files with at least one bank page: {len(empty_pages)}")
print(empty_pages)
df = pandas.DataFrame (sentences_list, columns=['file', 'sentence'])
df.to_csv(output_name,  encoding="utf-8", index=False)
