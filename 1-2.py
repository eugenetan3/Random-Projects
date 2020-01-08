import sys

def main(argument, argument2):
    perm = []

    string1 = sorted(argument)
    string2 = sorted(argument2)

    if string1 == string2:
        print("Yes")
        return True
    else:
        print("No")
        return False


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

        
        
