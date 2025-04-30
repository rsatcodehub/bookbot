from stats import count_words
from stats import count_characters


def get_book_text(filepath):  # Colon here after function definition
    with open(filepath) as f:  # Colon here after with statement
        return f.read()  # No colon after return statement


def main():  # Colon here after function definition
    book_text = get_book_text("books/frankenstein.txt")  # No colon after assignment
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document")

# Count characters and print result
    char_counts = count_characters(book_text)
    print("\nCharacter counts:") ## only the header
    for char, count in char_counts.items():
        print(f"'{char}': {count}") ## actual counts
  

# This line calls the main function when you run the script
main()  # No colon after function call

