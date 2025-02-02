def count_char_frequency(filepath):

    char_counts = {}

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            file_content = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None
 
    for char in file_content:
        char_lower = char.lower()
        if 'a' <= char_lower <= 'z':
            char_counts[char_lower] = char_counts.get(char_lower, 0) + 1

    return char_counts

def main():

    filepath = 'books/frankenstein.txt'
    result = count_char_frequency(filepath)

    if result:
        for char, count in result.items():
            print(f"The '{char}' character was found {count} times")

if __name__ == "__main__":
    main()