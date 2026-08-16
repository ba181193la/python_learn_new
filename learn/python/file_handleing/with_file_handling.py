from pathlib import Path
import csv
# with open("example.txt","r") as file:
#     for line in file:
#         print(line.strip())

# ******************************Read line*************************************


# feedback = input("enter feedback: ")
# file_path = Path(__file__).with_name("feedback.txt")

# with file_path.open("a", encoding="utf-8") as log:
#     log.write(feedback + "\n")

# print("thaks for feedback")
# ******************************************

# # read line
# file_path = Path(__file__).with_name("feedback.txt")
# with file_path.open("r", encoding="utf-8") as file:
#     print(file.readline().strip())


# ******************************while,for*************************************

# file_path = Path(__file__).with_name("feedback.txt")

# with file_path.open("r",encoding="utf-8") as file:
#     while True:
#         line=file.readline()
#         if not  line:
#             break
#         if "ERROR" in line:
#             print("Found Errors",line.strip())

# ******************************************

# for loop
# "_" throw away var there  don't given anything

# file_path = Path(__file__).with_name("feedback.txt")
# with file_path.open("r",encoding="utf-8") as file:
#     for _ in range(3):
#         print(file.readline().strip())


# ******************************CSV FILE READ*************************************

# with open ("sample.csv","r") as inline, open("outfile.csv","w") as outfile:
#     for line in inline:
#         print(line.strip())
#         outfile.write(line)
# ******************************************
# read_file_path = Path(__file__).with_name("sample.csv")

# with read_file_path.open ("r",encoding="utf-8") as inline, open("outfile.csv","w") as outfile:
#     for line in inline:
#         print(line.strip())
#         outfile.write(line)
# ******************************************

# read_file_path = Path(__file__).with_name("sample.csv")

# if not read_file_path.exists():
#     read_file_path.write_text("name,age\nAlice,25\nBob,30\n", encoding="utf-8")

# with read_file_path.open("r", encoding="utf-8", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["age"])
# ******************************************

read_file_path = Path(__file__).with_name("hello.csv")

with read_file_path.open('r',encoding="utf-8",newline="") as inline:
    lines=inline.readlines()
    print("all print", lines)
    print("skip print",lines[1:])

    for index, line in enumerate( lines[1: ]):  #skip header
        # print("inside loop",line)
        check=line.strip()
        print(index,"check", check)
        col=line.strip().split(",")
        print(index,"afterv split",col)
        print(index,col[1],col[2])
