# Write your code here
from nltk.tokenize import WhitespaceTokenizer

text_file = input('')
text = open(text_file, "r", encoding="utf-8").read()
wtc = WhitespaceTokenizer()
words = wtc.tokenize(text)
unique = set(words)

print("Corpus statistics")
print("All tokens: ", len(words))
print("Unique tokens: ", len(unique))
while True:
    index = input()

    if index == 'exit':
        break
    else:
        try:
            index = int(index)
            print(words[index])
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")
        except ValueError:
            print("Type Error. Please input an integer.")