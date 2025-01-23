
def totalwords(file_contents):
    words = file_contents.split()
    return len(words)

def total_characters(words):
    lowered_words = words.lower()
    character_dict = {}
    for char in lowered_words:
        if char.isalpha():
            if char in character_dict:
                character_dict[char] += 1
            else: 
                character_dict[char] = 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = totalwords(file_contents)
        character_counts = total_characters(file_contents)
        char_list = []
        for char, count in character_counts.items():
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print("--- End report ---")

main()


