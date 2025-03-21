
def word_counter(book_content):
    counter = 0
    
    total_words = book_content.split()
    for word in total_words:
        counter += 1
        
    return counter, total_words

def char_counter(book_content):
    dictionar = dict()
    
    for word in book_content:
        for char in word:
            if char == " ":
                continue
            char = char.lower()
            if char in dictionar:
                dictionar[char] += 1
            else:
                dictionar[char] = 1
    
    return dictionar
