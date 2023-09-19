# PastaHopper, expedite pasting items from a long list
import pyperclip, keyboard, time
from dataclasses import dataclass
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

@dataclass
class User():
    name: str
    email: str


if __name__ == "__main__":
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", default="input.txt", help="Path to line seperated input text file e.g. 'C:\some\\folder\input.txt'")
    parser.add_argument("-r", "--repeat", default=1, type=int, help="Number of times to paste an item before moving on")
    args = vars(parser.parse_args())

    # Open user.csv and read the rows into a list of User objects
    path = rf"{args['input']}"
    rep_number = args['repeat']
    dataList: [str] = []
    with open(path, 'r') as input:
        for line in input:
            dataList.append(line)
    
    print(f"Loaded {len(dataList)} items from {path}!")

    index = 0
    subindex = 1
    pyperclip.copy("")

    while True:
        keyboard.wait('ctrl+v')
        time.sleep(0.1)
        try:
            text = dataList[index].replace('\n', '')
            pyperclip.copy(text)
            print(f"Pasted ({subindex}/{rep_number}): {text}")
            # keyboard.write(f'record-add --title="Microsoft: {user_name}" --record-type=login login={user_email} password=$GEN url=https://login.microsoftonline.com')
            if subindex < rep_number:
                subindex += 1
            else:
                index += 1
                subindex = 1

        except(IndexError):
            pyperclip.copy("")
            break
    input.close()
    
    print("Script Done")