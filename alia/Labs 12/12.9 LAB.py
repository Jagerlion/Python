import csv
from collections import Counter

input_file = input()
with open(input_file,'r') as csvfile:
    input_reader = csv.reader(csvfile, delimiter=',')
    words = []

    for row in input_reader:
        words.extend(row)

word_count = {}
word_count = Counter(words)
for word, count in word_count.items():
    print(f'{word} - {count}')