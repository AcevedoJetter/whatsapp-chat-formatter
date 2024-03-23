# Whatsapp Chat Formatter

# Summary

When a chat is exported from Whatsapp, the output is a zip folder with a txt file

This GitHub repo changes the chat from a unreadable txt file to a csv file with the following columns: date, time, name, and message. The formatted csv file can be used for data analysis purposes

# main.py

`open_txt_file(filename)`

- Takes in a string which is the name of the txt file with the exported chat
- Returns a list with lists that each have a line of the conversation

`format_data(data)`

- Takes in what is returned from `open_txt_file(filename)` which is a list with lists that each have a line of the conversation
- Returns a pandas DataFrame with four columns: date, time, name, message where each row of the DataFrame contains a single message

# Running main.py

To run the file, run the following in the terminal:

`python3 main.py directory_path filename`

where `directory_path` is the path to the directory where `filename` is located. The common `filename` is `_chat.txt`. A new file will be created in the `directory_path` directory named `{filename}_formatted.csv` which contains the result of formatting the txt file into a readable csv.
