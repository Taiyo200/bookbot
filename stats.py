
def word_counter(book_content):
    counter = 0
    
    total_words = book_content.split()
    for word in total_words:
        counter += 1
        
    return counter

def char_counter(book_content):
    dictionar = dict()
    
    for word in book_content:
        for char in word:
            if char == " " or char == " \n ":
                continue
            char = char.lower()
            if char in dictionar:
                dictionar[char] += 1
            else:
                dictionar[char] = 1
    
    return dictionar

def pretty_display(counter, dictionar, book_path):
    
    listed_dictionary = [{"character": key, "count": value} for key, value in dictionar.items()]
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {counter} total words")
    print("--------- Character Count -------")
    
    listed_dictionary.sort(reverse=True, key=sort_on)
    for item in listed_dictionary:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")
            
    print("============= END ===============")
    
def sort_on(listed_dictionary):
    return listed_dictionary["count"]