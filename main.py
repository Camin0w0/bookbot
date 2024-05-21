def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = num_words(text)
    dictionary= my_dictionary(text)
    new_dictionary= sorted_dictionary(dictionary)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the file")
    for key, value in new_dictionary:
        print(f"The {key} character was found {value} times")
    print("--- End report ---")


def sorted_dictionary(dictionary):
    import operator
    new_list= sorted(dictionary.items(), key= operator.itemgetter(1), reverse= True)
    return new_list

def my_dictionary(text):
    from collections import Counter
    c = Counter()
    for line in text:
        low= line.lower()
        if low in "abcdfghiklmnopqrstuvwxyz":
            c += Counter(low)
    return c

def num_words(text):
    file = text.split()
    count = len(file)
    return count

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

main()
#with open("books/frankenstein.txt") as f:
    #words= f.read()
    #file= words.split()
    #num_words= len(file)
    #print(f"{num_words} words found in the file")