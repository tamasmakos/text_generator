from nltk import WhitespaceTokenizer, bigrams, trigrams
from collections import defaultdict, Counter
import random
import re

text = input()
file = open(text, "r", encoding="utf-8")
tokens = []

for line in file:
    for token in WhitespaceTokenizer().tokenize(line):
        tokens.append(token)
trigram = list(trigrams(tokens))

f = defaultdict(list)
for trigram in trigram:
    f[trigram[0] + " " + trigram[1]].append(trigram[2])

frequency = defaultdict(dict)
for key, value in f.items():
    frequency[key] = dict(Counter(value))


def text_generator(iterations):
    sentence = []

    def new_start():
        starting_word = random.choice(list(
            word for word in frequency.keys() if
            bool(re.match("[A-Z]", word[0])) and not bool(re.match("[!.?]", word.split()[0][-1]))))

        sentence.append(starting_word)
        sentence.append(random.choices(list(word for word in frequency[sentence[-1]].keys()), weights=(list(frequency[sentence[-1]].values())))[0])

    def next_word():
        word = random.choices(list(
            word for word in frequency[sentence[-2].split()[-1]+" "+sentence[-1]].keys()),
            weights=(list(frequency[sentence[-2].split()[-1]+" "+sentence[-1]].values())))[0]

        sentence.append(word)

    for i in range(iterations):
        new_start()
        count = 0
        while count < 6 or bool(re.match(".+[!.?]", sentence[-1])) is not True:
            next_word()
            for word in sentence:
                count += len(word.split())

        printable = " ".join(sentence)
        print(printable)

        sentence = []


text_generator(10)
