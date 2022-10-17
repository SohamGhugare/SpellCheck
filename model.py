# import nltk

from nltk.metrics.distance import jaccard_distance, edit_distance
from nltk.util import ngrams

# Run this line to download the words package from nltk
# nltk.download("words")
from nltk.corpus import words

correct_words = words.words()

# Gathering incorrect words, dummy words list vv
incorrect_words = ["amazinggg", "happpy", "intellignet"]

def spell_check(word: str):
    
    temp = [
        (jaccard_distance(set(ngrams(word.lower(), 2)), set(ngrams(w, 2))), w)
            for w in correct_words if w[0] == word.lower()[0]
    ]

    # temp = [(edit_distance(word, w),w) for w in correct_words if w[0]==word[0]]

    return sorted(temp, key=lambda val: val[0])[0][1]
