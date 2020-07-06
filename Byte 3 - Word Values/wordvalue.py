import urllib.request

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding

def load_words():
    with open("word_list.txt", "r", encoding="utf8") as file:
        word_list = [line.strip() for line in file]
    print(LETTER_SCORES)
    return word_list


def calc_word_value(word):
    score = 0
    for letter in list(word):
        if letter in LETTER_SCORES:
            print("first", letter)
            score += LETTER_SCORES[letter.upper()]
        else:
            print("second", letter)
            score += 0
    return score

def max_word_value(words):
    scores = []
    for word in words:
        scores.append(calc_word_value(word))
    """Given a list of words calculate the word with the maximum value and return it"""
    return words[scores.index(max(scores))]

print(max_word_value(['bob', 'julian', 'pybites', 'quit', 'barbeque']))


print(calc_word_value("bob"))
