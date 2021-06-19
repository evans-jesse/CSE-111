import csv
from os import replace

def main():
    text_list = read_list("provinces.txt")
    print(text_list)

    # print(f"Alberta shows up {} times in the modified list.")

def read_list(filename):
    text_list = []
    with open(filename, "rt") as text_file:
        csv_reader = csv.reader(text_file)
        next(csv_reader)
        for line in csv_reader:
            print(line)
    return text_list

if __name__ == "__main__":
    print("------------------------------------------\n")
    main()
    print("\n------------------------------------------")





