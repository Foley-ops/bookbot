from collections import Counter

PATH = "books/frankenstein.txt"

def main(book_path):
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents
        
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    return Counter(c for c in text.lower() if c.isalpha())

def run_report(book_path):
    print("--- Begin report of books/frankenstein.txt ---")
    wordcount = count_words(main(book_path))
    print(f"{wordcount} words found in the document\n")
    
    char_count = count_characters(main(book_path))
    
    for char, count in char_count.items():
        print(f"The '{char}' character was found {count} times")
        
    print("--- End of report ---")
    
    return

run_report(PATH)