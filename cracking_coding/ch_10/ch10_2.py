from collections import defaultdict


def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = "".join(sorted(word.lower()))
        anagrams[sorted_word].append(word)
    print(anagrams.values())
    sorted_words = []
    for similar_words in anagrams.values():
        sorted_words.extend(similar_words)
    return sorted_words


words = ["abed", "later", "bead", "alert", "altered", "bade", "alter", "alerted"]

print(group_anagrams(words))
