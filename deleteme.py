#!/usr/bin/env python
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines[1:]  # Skip the header line

def extract_book_titles(lines):
    book_titles = [line.split(',')[1].strip() for line in lines]
    return book_titles

def create_book_title_dict(book_titles):
    book_title_dict = {}
    index = 1
    for title in book_titles:
        if title not in book_title_dict.values():
            book_title_dict[index] = title
            index += 1
    return book_title_dict

# Usage example
file_path = 'reading_sessionz.txt'
lines = read_file(file_path)
book_titles = extract_book_titles(lines)
book_title_dict = create_book_title_dict(book_titles)

print("Book Title Dictionary:")
for index, title in book_title_dict.items():
    print(f"{index}: {title}")

