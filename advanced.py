"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    
    # generate a dictionary of the characters and counts, excluding spaces:
    # create an empty dictionary for these key(character)-value(count) pairs
    # iterating over the string (by character), add to the dictionary
    # if the character isn't already in the dictionary and isn't a space:
    #     add key to the dictionary and set value to 1
    # otherwise(character is already in the dictionary):
    #     add 1 to key's value
    character_counts = {}
    for character in input_string:
        if character == ' ':
            pass
        elif character not in character_counts:
            character_counts[character] = 1
        else:
            character_counts[character] += 1
    # print character_counts

    # convert dictionary into a list of tuples: [(count, character)...]
    character_counts_tupled = []
    for entry in character_counts:
        tuple = (character_counts[entry], entry)
        character_counts_tupled.append(tuple)

    # sort the list with highest numbers first
    #     sort the list, which should result in smallest character first
    #     then reverse
    character_counts_tupled.sort()
    character_counts_tupled = character_counts_tupled[::-1]
    # print character_counts_tupled

    # set the highest_count variable based on the first tuple in the list
    highest_count = character_counts_tupled[0][0]
    # print highest_count

    # create an empty list for the characters with the highest count
    # iterating over the list, 
    #     if the zeroth index(count) of the tuple matches the highest count:
    #         add first index (character) to highest count list
    # (could alternatively iterate over the original dictionary)
    highest_count_characters = []
    for character in character_counts_tupled:
        if character[0] == highest_count:
            highest_count_characters.append(character[1])
    # print highest_count_characters

    highest_count_characters.sort()

    # return the most common characters, sorted alphabetically
    return highest_count_characters

def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    # turn input list into a dictionary with key=word and value=word-length
    word_dict = {word: len(word) for word in words}
    # print "word_dict =", word_dict

    # iterating over the dictionary, 
    #     create a list of tuples (word-length, list of single word)
    initial_list = []
    # for entry in word_dict:
    #         initial_list.append((word_dict[entry], [entry, ]))
    for key, value in word_dict.iteritems():
        initial_list.append((value, [key, ]))

    sorted_list = sorted(initial_list)
    # print "initial_list =", initial_list
    # print "sorted_list =", sorted_list

    # collapse tuples with the same word-length:
    #     each tuple: word-length, sorted list of all words with that length
    final_list = []
    current_index = 0
    for item in sorted_list:
        if sorted_list[0] == item: 
            final_list.append(item)
            # print final_list  
        elif sorted_list[current_index][0] == sorted_list[current_index-1][0]:
            final_list[current_index-1] = (final_list[current_index-1][0], (final_list[current_index-1][1] + (sorted_list[current_index][1])))
            # print final_list
        else:
            final_list.append(item)       
            # print final_list
        current_index += 1

    return final_list


##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
