import sys

def main(string):
    if len(string) % 2 == 0:
        even = True
        dictionary = {}
        
        for letter in string:
            if letter not in dictionary:
                dictionary[letter] = 1
            else:
                dictionary[letter] += 1
               
        x = dictionary.keys()
        single = False 

        numSingles = 0
        for i in x:
            if dictionary[i] == 1:
                single = True
                numSingles += 1
            elif dictionary[i] > 2 and dictionary[i] % 2 != 0:
                print("False")
                return False
            

        if numSingles > 0:
            print("False")
            return False
        print("True") 
        return True
    elif len(string) % 2 != 0:
        odd = True
        dictionary = {}

        for letter in string:
            if letter not in dictionary:
                dictionary[letter] = 1
            else:
                dictionary[letter] += 1
        x = dictionary.keys()
        numSingles = 0

        for i in x:
            if dictionary[i] == 1:
                numSingles += 1
            elif dictionary[i] > 2 and dictionary[i] % 2 != 1:
                print("False")
                return False 
        if numSingles == 1 and len(x) == 1:
            print("True")
            return True
        elif numSingles > 1:
            print("False")
            return False
        print("True")
        return True
        


if __name__ == '__main__':
   main(sys.argv[1]) 
