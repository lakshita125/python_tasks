# Create a set of words from a text file and count the occurrence of each word in the set
def count_words_in_file(file_path):
    word_set = set()
    word_counts = {}

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                cleaned_word = word.strip().lower()
                if cleaned_word:
                    word_set.add(cleaned_word)
                    word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1

    return word_set, word_counts

# Example usage:
file_path = 'C:\\Users\\Admin\\Desktop\\file.txt.txt'
unique_words, word_occurrences = count_words_in_file(file_path)

# Output the unique words and their occurrences
print("Unique Words:", unique_words)
print("Word Occurrences:", word_occurrences)
