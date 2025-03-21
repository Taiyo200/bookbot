
def word_counter(book_content):
    counter = 0
    total_words = book_content.split()
    for word in total_words:
        counter += 1
    return counter