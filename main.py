def get_book_text(filepath):  # Colon here after function definition
    with open(filepath) as f:  # Colon here after with statement
        return f.read()  # No colon after return statement

def count_words(text):
    words = text.split()     # Split the text into words
    word_count = len(words)
    return word_count


def main():  # Colon here after function definition
    book_text = get_book_text("books/frankenstein.txt")  # No colon after assignment
    word_count = count_words(book_text)
    print(f"{word_count} words found in the book")
    


# This line calls the main function when you run the script
main()  # No colon after function call

