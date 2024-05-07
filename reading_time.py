#!/usr/bin/env pythonL
import re
from math import ceil
import datetime
from textwrap import dedent
from text_art import thing

# GPT4
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

""" 
REDO THIS SHIT FUNCTION!!
"""
def get_input(new_book=False):
    """
    Gets user input as book number.
    """
    tries = 0
    while tries < 3:
        tries += 1

        if not new_book:
            user = input(dedent("""
\n\n
Enter book number:
Press '0' (zero) to enter a new book
                                """))
            # Ensure input is numeric
            if user.isnumeric():
                return int(user)

            else:
                print("Invalid input, please try again: (◕‿◕)╭∩╮\n")
                
        else:
            user = input("\n\nEnter book title: (◕‿◕)╭∩╮\n")
            # Ensure input is alphabetic 
            return user

    print(thing)

def get_book_from_user():
    """
    Either selects an existing book title or provides a new entry.
    To replace the get_input function.
    ---------------------------------------------
    User: enter the index number of book OR '0' for a new book entry
    Convert str to integer (input: int only) using try, exception blocks
    Ensure valid entry (ew) for OUTPUT
    """
    user_input = int(input(dedent("""
Please select a book from the list by entering the index number 
(Press 0 for new entry (ew)):
                                  """)))
    

def output_book_list(books):
    """
    Provides book list for user to select the given index for the corresponding
    book title, unless it must be added.
    --------------------------------------------------------
    Input:
        books: (dict)

    Ouput:
        None
    """
    for idx, title in books.items():
        print(f"[{idx}]: {title}")

    return None

def output_selection(key, books):
    """
    Output the selected book title.
    -------------------------------
    Input:
        key: (int)
        book title: (str)

    Output:
        selected book titile: (str)
    """
    return books[key]

def create_book(book_title ,books):
    """
    Takes user input and creates a book title.
    ---------------------------------
    Input:
        book_title: (str) 
        books: (dict)

    Output:
        books: (dict) with new index and title added.

    """
    idx = list(books.keys())
    new_indx = idx[-1] + 1
    
    books[new_indx] = book_title
    print(f"New book added: {new_indx}: {book_title}")

    return books

def input_validation():
    """
    Gets user input of a single integer, then outputting that integer.
    -------------------------
    Input:
        None

    Output:
        key: key to a key-value pair (str)
    """

    try:
        key = int(input("""Enter the number associated with the book: """))

    except ValueError as e:
        print(f"Incorrect input: {e}\n try again: ")

        try:
            key = int(input("""Enter the number associated with the book: """))

        except ValueError as e:
            print(f"You're plenty ( ͡° ͜ʖ ͡°  ) stupid aren't ya... ")

            return "(◕‿◕)╭∩╮"

    return key

# Function to convert mixed numbers or pure numbers to float
def convert_string(string):
    try:
        parts = string.split()
        if len(parts) == 1:
            return float(parts[0])
        elif len(parts) == 2:
            whole_number = int(parts[0])
            numerator, denominator = map(int, parts[1].split('/'))
            return whole_number + numerator / denominator
        else:
            raise ValueError("Invalid input format")
    except (ValueError, ZeroDivisionError) as e:
        print(f"An error occurred: {e}")
        return None

#def convert_string(string):
#
#    try:
#        parts = string.split()
#        whole_number, fraction = int(parts[0]), parts[1]
#        numerator, denominator = map(int, fraction.split('/'))
#
#        return whole_number + numerator / denominator
#
#        return float(string)
#
#    except ValueError as e:
#        print(f"An error occurred: {e}")
#
#        return None

# Main function to calculate and save the reading rate
def calculate_reading_rate():
    """
    Calculates the reading rate by ... ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) 
    """
    pages_read = convert_string(input("Enter the number of pages you have read: "))
    less_than_hour = input("Did you read for less than an hour? (yes/no): ").strip().lower()

    if less_than_hour == "yes":
        hours_spent = 0
        minutes_spent = convert_string(input("Enter the number of minutes spent reading: "))

    else:
        hours_spent = convert_string(input("Enter the number of full hours spent reading: "))
        minutes_spent = convert_string(input("Enter the number of additional minutes spent reading: "))

    total_time_spent_hours = hours_spent + (minutes_spent / 60)
    reading_rate = pages_read / total_time_spent_hours
    print(f"Your reading rate is {reading_rate:.2f} pages per hour.")
    
    book_name = input("Enter the name of the book you are reading: ").strip()
    save_reading_session(book_name, pages_read, total_time_spent_hours, reading_rate)
    number_of_reading_sessions(reading_rate)

# Function to save reading session to a file
def save_reading_session(book_name, pages_read, hours_spent, reading_rate):
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    session_data = f"{date_str}, {book_name}, {pages_read}, {hours_spent:.2f}, {reading_rate:.2f}\n"

    with open("reading_sessionz.txt", "a") as file:
        file.write(session_data)
    print("Reading session saved.")
    print(f"CURRENTLY USING FAKE OUTPUT TO DATA!")

# Function to calculate the number of 30-minute sessions required based on reading rate
def number_of_reading_sessions(reading_rate):
    pages_to_read = convert_string(input("Enter the number of pages you need to read: "))
    total_reading_time_hours = pages_to_read / reading_rate
    sessions_needed = ceil((total_reading_time_hours * 2))  # 0.5 hour sessions
    print(f"You will need {sessions_needed} reading sessions to complete your reading.")

# Function to remove text within parentheses and count words, handling hyphens
def remove_text_within_parentheses_count_words_handle_hyphens(input_string):
    input_string = re.sub(r'\([^()]*\)', '', input_string)
    input_string_without_hyphens = re.sub(r'-', ' ', input_string)
    words = re.findall(r'\b[a-zA-Z][a-zA-Z0-9_]*\b', input_string_without_hyphens)
    word_count = len(words)

    return input_string_without_hyphens, word_count

# Function to read from text file and process for word count
"""
Fix this!! 
I need to count the number of RELEVANT words in a textfile.
"""
def process_file_for_word_count():
    file_path = input("Enter the text file to be read: ")

    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

    cleaned_string, word_count = remove_text_within_parentheses_count_words_handle_hyphens(file_contents)
    print(f"Cleaned string: {cleaned_string}")
    print(f"Word count: {word_count}")

def main():
    file_path = 'reading_sessionz.txt'
    lines = read_file(file_path)
    book_titles = extract_book_titles(lines)
    book_title_dict = create_book_title_dict(book_titles)

    print("Book Title Dictionary:")
    output_book_list(book_title_dict)

    book = ""
    book_not_selected = True
    while book_not_selected:
        user_input = get_input()

        if user_input is None:
            break

        if user_input == 0:
            book = get_input(new_book=True)

            if book is not None:
                book_title_dict = create_book(book, book_title_dict)
                book_not_selected = False

        else:

            book = get_input()
            book_not_selected = False
            print(f"Selected book: {book}")

        """
        ? --> Fix this plz ...  ʘ‿ʘ
        """
    breakpoint()
    calculate_reading_rate()

# Main script logic
if __name__ == "__main__":
    main()

#    check = input(
#"""Did you check the 'reading_session.txt' file?
#                  (y/n)""").lower()
#
#    if check == "y":
#        calculate_reading_rate()  # To calculate reading rate and manage reading sessions
#    #    process_file_for_word_count()  # To process a text file for word count
#
#    else:
#        print("Eat shit   (◕‿◕)╭∩╮")
#        exit()
#


