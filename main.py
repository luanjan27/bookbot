def main():
    hashmap = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        for w in words:
            for char in w:
                char = char.lower()
                if char in hashmap:
                    hashmap[char] += 1
                else:
                    hashmap[char] = 1
    return hashmap, word_count
            
hashmap, word_count = main()

def report(hashmap: dict, word_count: int):
    print("--- Begin report of books/frankenstein/txt ---")
    print(f"{word_count} words found in the document\n")
    for key, value in sorted(hashmap.items(), key=lambda item: item[1], reverse=True):
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    return None

report(hashmap, word_count)
