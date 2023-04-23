import sys

names = ["joshua", "Ron", "Divine", "Begati", "Isaiah", "Irabor", "Comfort"]

name = input("Name: ")

for n in names:
    if name == n:
        print("Name found!!!")
        sys.exit(0)

print("Not Found!!")
sys.exit(1)
