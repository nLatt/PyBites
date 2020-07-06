import urllib.request

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding

def load_words():
    with open (DICTIONARY,"r") as file:
        word_list = [line.strip() for line in file]
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    return word_list


def calc_word_value(word):
    score = 0
    for letter in list(word):
        try:
            score += LETTER_SCORES[letter.upper()]
        except:
            score += 0
    """Given a word calculate its value using the LETTER_SCORES dict"""
    return score

def max_word_value(words):
    scores = []
    for word in words:
        scores.append(calc_word_value(word))
    """Given a list of words calculate the word with the maximum value and return it"""
    return words[scores.index(max(scores))]
