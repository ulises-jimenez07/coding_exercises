"""
Count Word Frequency
Define a function to count the frequency of words in a given list of words.

Example:

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
count_word_frequency(words)
Output:

 {'apple': 3, 'orange': 2, 'banana': 1}

"""


def count_word_frequency(words):
    # TODO
    word_cnt = {}
    for word in words:
        if word in word_cnt:
            word_cnt[word] += 1
        else:
            word_cnt[word] = 1
    return word_cnt
