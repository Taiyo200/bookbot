from stats import *

def get_book_text(book_path):
    with open(book_path) as book:
         book_content = book.read()
    return book_content

def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path) 
    counter, total_words = word_counter(book_content)
    book_chars = char_counter(book_content)
    #print (f"Contents of the book: {book_content}")
    #print(f"{counter} words found in the document")
    print (book_chars)
    
main()