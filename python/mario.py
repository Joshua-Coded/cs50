def main():
    height = get_height()
    for i in range(height):
        print("#")


def get_height():
    while True:
        try:
            s = int(input("Give me height: "))
            if s > 0:     
                return s
        except ValueError:
            print("NOt an integer")

main()
