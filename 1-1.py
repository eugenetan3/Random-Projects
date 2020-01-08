
import sys

def main(word):
    store = []
    for w in word:
        if w in store:
            print("Nonunique characters\n")
            return False
        else:
            store.append(w)
    
    
    print("Unique characters\n")
    return True


if __name__ == '__main__':
    main(sys.argv[1])

    
