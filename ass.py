import nltk
from collections import Counter

nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words=set(stopwords.words('english'))
#print(stop_words)
nltk.download('punkt')
from nltk.tokenize import word_tokenize,sent_tokenize
#***
def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

file_path =( r"paragraphs.txt")
text = read_text_file(file_path)
#if text:
  #  print("File contents:")
 #   print(text)
#***

tokenized_word=word_tokenize(text)
#print(tokenized_word)


without_stopwords=[]
for word in tokenized_word:
  if word not in stop_words:
    without_stopwords.append(word)
#print('length of text',len(tokenized_word))
#print('length of processed text',len(without_stopwords))



# Count the frequency of each word
word_counts = Counter(without_stopwords)

#Print the frequency of each word
for word, count in word_counts.items():
    print(f"{word}: {count}")
