import nltk

from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams

# Run this line to download the words package from nltk
# nltk.download("words")
from nltk.corpus import words

correct_words = words.words()