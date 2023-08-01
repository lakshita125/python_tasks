''' Create a dictionary of book titles and the irrespective authors , write a Python program
that allows users to search for books by entering either the title or author's '''
def search_books(books_dict, query):
    results = {}
    for title, author in books_dict.items():
        if query.lower() in title.lower() or query.lower() in author.lower():
            results[title] = author
    return results


books_data = {
    'life story': 'lakshita sinha',
    'love story': 'navpreet kaur,harshita sharma',
    'Clean Code': 'rishav agarwal',
    'the world': 'atul soni'
}

# User input 
search_query = input("Enter a book title or author's name to search: ")

# Search for books matching the query
search_results = search_books(books_data, search_query)


if search_results:
    print("Search results:")
    for title, author in search_results.items():
        print(f"Book Title: {title}, Author: {author}")
else:
    print("No matching books found for the given query.")
