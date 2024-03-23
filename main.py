########################################
###      Fomat WhatsApp chat data    ### 
########################################

import sys
import pandas as pd

def open_txt_file(filename):
    """
    parameters:
        filename (string): txt file to open and read

    returns:
        data (list[list]): list with lists that each have a line of conversation
    """
    # Open txt file and get all the lines in filename
    f = open(filename, "r")
    return f.readlines()


def format_data(data):
    """
    parameters:
        data (list[list]): list with lists that each have a line of conversation

    returns:
        pandas DataFrame: txt file as a pd DataFrame
    """
    formatted_data = []
    line_to_add = []
    for line in data:
        no_new_line = line.replace("\n", "")
        if no_new_line != "":
            if (no_new_line[0] == "[" and no_new_line[1].isnumeric()) or no_new_line[0] == "\u200e":
                formatted_data.append(line_to_add)
                line_to_add = ""
                date = no_new_line.split(",")[0][1:].replace("[", "")

                line2 = no_new_line[len(date)+3:]
                time = line2.split("]")[0]

                line3 = line2[len(time)+2:]
                name = line3.split(":")[0]

                line4 = line3[len(name)+2:]
                message = line4

                line_to_add = [date, time, name, message]
            else:
                line_to_add[-1] += no_new_line

    return pd.DataFrame(formatted_data, columns=["date", "time", "name", "message"]).iloc[1: , :]


############################################
### Save the Formatted TXT file as a CSV ###
############################################
if __name__ == "__main__":
    directory = "".join(sys.argv[1])
    filename = "".join(sys.argv[2])
    formatted_data = format_data(open_txt_file(f"{directory}/{filename}"))
    actual_filename = filename.split(".txt")[0]
    formatted_data.to_csv(f"{directory}/{actual_filename}-formatted.csv", index=False)
