from src.distance import distance

def distance_test():
    word1 = "*ucking"
    word2 = "fucking"
    assert distance(word1, word2) == 1
    word1 = "fcking"
    word2 = "fucking"
    assert distance(word1, word2) == 1
    word1 = "ffucking"
    word2 = "fucking"
    assert distance(word1, word2) == 1