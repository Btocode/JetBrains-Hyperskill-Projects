# Write your code here
from nltk.tokenize import WhitespaceTokenizer
from nltk.util import bigrams

text_file = input('')
text = open(text_file, "r", encoding="utf-8").read()
wtc = WhitespaceTokenizer()
words = wtc.tokenize(text)

bg = list(bigrams(words))
unique = set(words)

print(f"Number of bigrams: {len(bg)}")
while True:
    index = input()

    if index == 'exit':
        break
    else:
        try:
            index = int(index)
            print(f'Head: {bg[index][0]} \t Tail: {bg[index][1]}')

        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")
        except ValueError:
            print("Type Error. Please input an integer.")