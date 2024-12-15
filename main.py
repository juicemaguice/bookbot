def main():
    path = "books/frankenstein.txt"
    book = get_book_content(path)
    char_count, word_count = get_character_count(book), get_word_count(book)

    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    print("\tfrequency of letters (from most to least common):")

    for i in range(len(char_count)): #prints sorted greatest to least by value
        current_max, max_char = float("-inf"), ""
        for char in char_count:
            if char_count[char] > current_max:
                current_max = char_count[char]
                max_char = char
        print(f"The \'{max_char}\' character is used {current_max} times")
        #print(f"\t\tdeleting {max_char}")
        del char_count[max_char]

    print("--- End of report ---")

    return None

def get_book_content(book_path):
    with open(book_path) as f:
        return f.read()
    return None

def get_word_count(text):
    split_text = text.split()
    return len(split_text)

def get_character_count(text):
    text, alpha = list(text.lower()), "abcdefghijklmnopqrstuvwxyz"
    characters = {}
    for c in text:
        if c in alpha:
            if c not in characters:
                characters[c] = 1
            else:
                characters[c] += 1
    return characters

main()