from nltk.tokenize import sent_tokenize
import os 
import PyPDF2
import pandas

# UNcomment to download the punkt dataset for the nltk package.
# ___________________________________
# import nltk
# nltk.download('punkt')
# ___________________________________


folder = ""
Key_words = []
save_file = ""

sentences_list = []
empty_pages = set()

files = os.listdir(folder)
files = [file for file in files if file.lower().endswith(".pdf")] #check if valid path
for file in files:
    pdf_submission = PyPDF2.PdfReader(f"{folder}/{file}") #use os.path.join
    for page in pdf_submission.pages:
        page_text = page.extractText()
        tokenize_sentence = sent_tokenize(page_text)
        if len(tokenize_sentence) == 0:
            empty_pages = empty_pages.union({file})
        sentences = [[file, sentence] for sentence in tokenize_sentence if any(word in sentence for word in Key_words)]
        sentences_list = sentences_list + sentences

print(f"Number of file with at least one bank page: {len(empty_pages)}")
print(empty_pages)
df = pandas.DataFrame (sentences_list, columns = ['file', 'sentence'])
df.to_csv(save_file,  encoding= "utf-8", index= False)
