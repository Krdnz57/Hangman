import random

path = 'wordlist.txt'


def get_random_word_from_file():
    num_words_processed = 0
    curr_word = None
    with open(path, 'r') as f:
        for word in f:
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                curr_word = word
    return curr_word