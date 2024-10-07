def read_synonyms(filename):
    synonyms_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for w in words:
                first_letter = w[0]
                if first_letter not in synonyms_dict:
                    synonyms_dict[first_letter] = []
                synonyms_dict[first_letter].append(w)
    return synonyms_dict


def find_synonyms(synonyms_dict, word, letter):
    if letter in synonyms_dict:
        for synonym in synonyms_dict[letter]:
            print(synonym)
    else:
        print(f'No synonyms for {word} begin with {letter}.')


def main():
    word = input()
    letter = input()
    
    filename = word + '.txt'
    synonyms_dict = read_synonyms(filename)
    find_synonyms(synonyms_dict, word, letter)


if __name__ == "__main__":
    main()