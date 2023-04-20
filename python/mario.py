def main():
    height = get_height()
    for i in range(height):
        print("#")


def get_height():
    while True:
        s = int(input("Give me height: "))
        return s

main()
