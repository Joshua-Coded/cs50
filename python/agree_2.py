s = input("DO you agree? ")

if s.lower() in ["y", "yes"]:
    print("Agreed. ")
elif s.lower() in ["n", "no"]:
    print("Not agreed. ")
else:
    print("Invalid input")
