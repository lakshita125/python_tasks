''' Given a list of strings , write a function to find the two string with the highest 
 similarity score. Thes imilarity score is defined as the number of common characters between two strings '''
def similarity_score(string1, string2):
    return len(set(string1) & set(string2))

def find_highest_similarity_score(strings):
    max_score = 0
    highest_similarity_strings = None

    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            score = similarity_score(strings[i], strings[j])
            if score > max_score:
                max_score = score
                highest_similarity_strings = (strings[i], strings[j])

    return highest_similarity_strings

# Example usage:
string_list = ["laksh","harsh","nav","atul" ,"shivam"]
result = find_highest_similarity_score(string_list)
print("Strings with the highest similarity score:", result)




 