import sys


def main(stringspace, strlength):
    hold = []

    for i in range(int(strlength)):
        if stringspace[i] == ' ':
            hold.append("%20")
        else:
            hold.append(stringspace[i])

    string = ''.join(hold)
    print(string)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
