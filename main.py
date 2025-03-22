from stats import *
import sys

def get_book_text(book_path):
    with open(book_path) as book:
         book_content = book.read()
    return book_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    #book_path = "books/frankenstein.txt"
    book_content = get_book_text(book_path) 
    counter = word_counter(book_content)
    dictionar = char_counter(book_content)
    pretty_display(counter, dictionar, book_path)
    #print (f"Contents of the book: {book_content}")
    #print(f"{counter} words found in the document")
    #print (book_chars)
    
main()