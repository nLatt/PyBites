import urllib.request

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding

def load_words():
    with open("word_list", "r", encoding="utf8") as file:
        word_list = [line.strip() for line in file]
    return word_list


def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    pass


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    pass