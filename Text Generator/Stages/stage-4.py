from collections import Counter, defaultdict
from nltk.tokenize import WhitespaceTokenizer
from nltk.util import bigrams
import random

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


markov_dct = build_markov_model(bg)


def generate_text(markov_dict):
    first_word = random.choice(list(markov_dict.keys()))
    stopper = True
    count = 0
    while stopper:
        sentence = first_word
        next_word = first_word
        complete_sentence = False
        while not complete_sentence:
            if len(sentence.split()) < 10:
                item = markov_dict[next_word]
                if list(item.keys()):
                    next_word = random.choices(population=list(item.keys()), weights=list(item.values()))[0]
                    sentence += f' {next_word}'
            else:
                complete_sentence = True
        if len(sentence.split()) == 10:
            print(sentence.strip())
            count = count + 1
        if count == 10:
            stopper = False
        first_word = next_word


generate_text(markov_dct)
