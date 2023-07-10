# Whatsapp Chat Cleaner

# Basics

When a chat is exported from Whatsapp, the output is a zip folder with a txt file

This GitHub repo cleans the chat and saves it to a csv file

# cleaner.py

open_txt_file(filename)

- Takes in a string which is the name of the txt file with the exported chat
- Returns a list with lists that each have a line of the conversation

cleaner(data)

- Takes in a list with lists that each have a line of the conversation
- Returns a pandas DataFrame with four columns: date, time, name, message where each row of the DataFrame contains a single message

# Running cleaner.py

To run the file, run the following in the terminal:

`python3 cleaner.py directory_path filename`

where `directory_path` is the path to the directory where `filename` is located. The common `filename` is `_chat.txt`
