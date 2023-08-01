''' Create a function that takes a list of words and groups them into a
dictionary based on the length of each word '''
def group_words_by_length(word_list):
    word_dict = {}
    for word in word_list:
        length = len(word)
        if length in word_dict:
            word_dict[length].append(word)
        else:
            word_dict[length] = [word]
    return word_dict


words_list = ['dog', 'cat', 'bear', 'elephant', 'deer']

# Group the words by their lengths
grouped_dict = group_words_by_length(words_list)


print("Words grouped by their lengths:")
print(grouped_dict)
