def count_words(text):
    words = text.split()     # Split the text into words
    word_count = len(words)
    return word_count

def count_characters(text):
    # Convert all text to lowercase
    text = text.lower()
    
    # Create an empty dictionary to store character counts
    char_count = {}
    
    # Loop through each character in the text
    for char in text:
        # Check if character is already in our dictionary
        if char in char_count:
            # If it is, increment its count
            char_count[char] += 1
        else:
            # If it's not, add it with a count of 1
            char_count[char] = 1
    
    # Return the completed dictionary
    return char_count
