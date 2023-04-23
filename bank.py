# Author: Alana Joshua
# This program prompt user for input
# if "index[0]" print $20
#elif "index[input > 0]" print "$100"
#else print "$0"


x = input("Tell me something ").lower()

if x.startswith("hello"):
    print("$0")
elif x.startswith("h"):
    print("20")
else:
    print("$100")
