
import difflib
import csv
import os
import argparse



parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument('filename')           # positional argument
parser.add_argument("game_number")  # on/off flag

args = parser.parse_args()




KNOWN_FILES = ["aggregated_1.csv", "aggregated_2.csv", "playername_to_code.csv"]


for file in os.listdir("data"):
    print("Detected file:", file)





PLAYER_MAPPING = "data/playername_to_code.csv"



def read_csv_into_list(file_path):
    data_list = []
    with open(file_path, newline='', encoding='utf8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            data_list.append(row)
    return data_list





player_to_code = {}

for lis in read_csv_into_list(PLAYER_MAPPING):
    a, b = lis
    player_to_code[a.lower()] = b



def get_player_code(pname):
    '''
    returns None on invalid!
    '''
    pname = pname.lower()
    if pname in player_to_code:
        return player_to_code[pname]
    return None



print(get_player_code("BMAli"))
print(get_player_code("BmAli"))
print(get_player_code("bMAli"))



words = ['hello', 'Hallo', 'hi', 'house', 'key', 'screen', 'hallo', 'question', 'format']
difflib.get_close_matches('Hello', words)


