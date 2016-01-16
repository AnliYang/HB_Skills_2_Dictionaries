"""Skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""

import collections


def without_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    # to de-dupe, turn the list into a set
    return set(words)


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not use 'if ___ in ___' or the method 'index'.

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([4, 3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    """

    # set math: intersection between two lists 
    return list(set(list1) & set(list2))


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    # convert input_string to list
    # use Counter on converted list
    return collections.Counter(input_string.split(' '))

    # FIXME: do it the long way, too (as in the first Dictionary exercise)


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    # create a dictionary for English-->Pirate translations
    trans_eng_to_pirate = {
                            "sir": "matey",
                            "hotel": "fleabag inn",
                            "student": "swabbie",
                            "boy": "matey",
                            "madam": "proud beauty",
                            "professor": "foul blaggart",
                            "restaurant": "galley",
                            "your": "yer",
                            "excuse": "arr",
                            "students": "swabbies",
                            "are": "be",
                            "lawyer": "foul blaggart",
                            "the": "th'",
                            "restroom": "head",
                            "my": "me",
                            "hello": "avast",
                            "is": "be",
                            "man": "matey",                         
    }
    
    # convert input phrase (str) to a list
    phrase = phrase.split(' ')

    # create a new "translated" list, iterating over the original list
    #     to translate (or leave alone if the word isn't translatable)
    translation = []

    for word in phrase:
        if word in trans_eng_to_pirate:
            translation.append(trans_eng_to_pirate[word])
        else:
            translation.append(word)

    # convert the new list back into a string
    final_translation = ' '.join(translation)

    return final_translation


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items---the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """

    # create a dictionary, iterating over the original list of words:
    #     keys are the word length and values are a word
    #     if the key already exists, you add to the list of values
    word_lengths_dict = {}

    for word in words:
        if len(word) in word_lengths_dict:
            word_lengths_dict[len(word)].append(word)
        else:
            word_lengths_dict[len(word)] = [word]
    
    # create a list, iterating over your dictionary to 
    #     convert each entry to a tuple
    word_lengths_list = []

    for entry in word_lengths_dict:
        word_lengths_list.append((entry, word_lengths_dict[entry]))

    # sort your list by key and return that
    word_lengths_list.sort()

    return word_lengths_list
    # FIXME seems wasteful to be iterating over it all twice,
        # come back to try refactoring
        # if not to iterate only once, do the second as a list comprehension
        # for fun


def get_sum_zero_pairs(input_list):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    # if the number's opposite exists in input list, or if the number is 0,
    #     add the pair to pairs list if it's not already in there
    sum_zero_pairs = []

    for number in input_list:
        if (number * -1) in input_list:
            pair = sorted([(number * -1), number])
            if pair not in sum_zero_pairs:
                sum_zero_pairs.append(pair)
    
    # sort the list
    sum_zero_pairs = sorted(sum_zero_pairs)

    return sum_zero_pairs


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
