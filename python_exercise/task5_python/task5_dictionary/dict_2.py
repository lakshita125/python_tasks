'''Write a Python program that takes a sentence as input and counts
   the frequency of each word using a dictionary '''
def count_word_frequency(sentence):
    word_frequency = {}
    words = sentence.split()

    for word in words:
        # Remove any punctuation marks from the word
        word = word.strip(".,!?\"'()[]{}:;-")

        # Convert the word to lowercase to treat words case-insensitively
        word = word.lower()

        # Increment the count of the word in the dictionary
        word_frequency[word] = word_frequency.get(word,0) + 1

    return word_frequency

# Example usage:
user_sentence = input("Enter a sentence: ")
word_freq_dict = count_word_frequency(user_sentence)

print("Word frequency in the sentence:")
for word, freq in word_freq_dict.items():
    print(f"{word}: {freq}")
   