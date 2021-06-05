
from collections import Counter, defaultdict
from nltk.tokenize import WhitespaceTokenizer
from nltk.util import bigrams, trigrams
import random

text_file = input('')
text = open(text_file, "r", encoding="utf-8").read()
wtc = WhitespaceTokenizer()
words = wtc.tokenize(text)

bg = list(bigrams(words))
tg = list(trigrams(words))


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
def markov_tri_model(trigrams):
    markov_dict = defaultdict(list)
    for i in trigrams:
        markov_dict[i[0] + " " + i[1]].append(i[2])

    for k, v in markov_dict.items():
        markov_dict[k] = Counter(v)
    return markov_dict


markov_dct = build_markov_model(bg)


def execute_stage_4(markov_dict):
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
                elif next_word[-1] not in [".", "!", "?"]:
                    item = markov_dict[next_word]
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
            while not first_word[0].isupper() or first_word[-1] in [".", "!", "?"]:
                first_word = random.choice(list(markov_dict.keys()))


def execute_stage_5(markov_dict):
        first_word = random.choice(list(markov_dict.keys()))
        while not first_word[0].isupper() or first_word[-1] in [".", "!", "?"]:
            first_word = random.choice(list(markov_dict.keys()))

        for i in range(10):
            sentence = first_word
            next_word = first_word
            complete_sentence = False
            while not complete_sentence:
                if len(sentence.split()) < 5:
                    item = markov_dict[next_word]
                    if list(item.keys()):
                        next_word = random.choices(population=list(item.keys()), weights=list(item.values()))[0]
                        sentence += f' {next_word}'
                elif next_word[-1] not in [".", "!", "?"]:
                    item = markov_dict[next_word]
                    next_word = random.choices(population=list(item.keys()), weights=list(item.values()))[0]
                    sentence += f' {next_word}'
                else:
                    complete_sentence = True
            print(sentence.strip())
            first_word = next_word
            while not first_word[0].isupper() or first_word[-1] in [".", "!", "?"]:
                first_word = random.choice(list(markov_dict.keys()))

def execute_final_stage(markov_dict):
        first_word = random.choice(list(markov_dict.keys()))
        while not first_word[0].isupper() or first_word.split()[0][-1] in [".", "!", "?"]:
            first_word = random.choice(list(markov_dict.keys()))

        for i in range(10):
            sentence = first_word
            next_word = first_word
            complete_sentence = False
            while not complete_sentence:
                if len(sentence.split()) < 5:
                    item = markov_dict[next_word]
                    if list(item.keys()):
                        next_word = random.choices(population=list(item.keys()), weights=list(item.values()))[0]
                        sentence += f' {next_word}'
                        next_word = sentence.split()[-2] + " " + sentence.split()[-1]
                elif next_word[-1] not in [".", "!", "?"]:
                    item = markov_dict[next_word]
                    next_word = random.choices(population=list(item.keys()), weights=list(item.values()))[0]
                    sentence += f' {next_word}'
                    next_word = sentence.split()[-2] + " " + sentence.split()[-1]
                else:
                    complete_sentence = True
            print(sentence.strip())
            first_word = next_word
            while not first_word[0].isupper() or first_word.split()[0][-1] in [".", "!", "?"]:
                first_word = random.choice(list(markov_dict.keys()))


#execute_stage_4(markov_dct)
#execute_stage_5(markov_dct)
execute_final_stage(markov_tri_model(tg))