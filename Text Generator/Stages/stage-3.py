from collections import Counter, defaultdict
from nltk.tokenize import WhitespaceTokenizer
from nltk.util import bigrams

text_file = input('')
text = open(text_file, "r", encoding="utf-8").read()
wtc = WhitespaceTokenizer()
words = wtc.tokenize(text)

bg = list(bigrams(words))


def tuple_to_dict(bglist):
    temp = dict()
    for a, b in bglist:
        temp.setdefault(a, []).append(b)
    return temp


def build_markov_model(grams):
    mk_dict = defaultdict(list)
    for i in grams:
        mk_dict[i[0]].append(i[1])
    for k, v in mk_dict.items():
        mk_dict[k] = Counter(v)

    return mk_dict


markov_dict = build_markov_model(bg)

while True:
    word = input()

    if word == 'exit':
        break
    else:
        try:
            print(f"Head: {word}")
            if word in markov_dict:
                for item in markov_dict[word].most_common():
                    print(f"Tail: {item[0]} \t Count: {item[1]}")
                print()
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")
        except ValueError:
            print("Type Error. Please input an integer.")
        except KeyError:
            print("The requested word is not in the model. Please input another word.")