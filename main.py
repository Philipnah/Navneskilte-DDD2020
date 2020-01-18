# We create the letters structure here in the order M, I, R, K, O
line1 = ["## ##", "#####", "#### ", "#   #", " ### "]
line2 = ["# # #", "  #  ", "#   #", "#  # ", "#   #"]
line3 = ["# # #", "  #  ", "#### ", "###  ", "#   #"]
line4 = ["#   #", "  #  ", "#   #", "#  # ", "#   #"]
line5 = ["#   #", "#####", "#   #", "#   #", " ### "]

# We create the main function here

def mainfunc():
    i = 0
    while i <= 4:
        print(line1[i] + " ", end="")
        i += 1

    print("")
    i = 0
    while i <= 4:
        print(line2[i] + " ", end="")
        i += 1

    print("")
    i = 0
    while i <= 4:
        print(line3[i] + " ", end="")
        i += 1

    print("")
    i = 0
    while i <= 4:
        print(line4[i] + " ", end="")
        i += 1

    print("")
    i = 0
    while i <= 4:
        print(line5[i] + " ", end="")
        i += 1

def printLetter():
    i = 0
    letters = input()
    
    individualLetters = letters.split()
    print(individualLetters[0])

    if individualLetters[0] == "m" or "M":
        i = 0

    if individualLetters[0] == "i" or "I":
        i = 1

    if individualLetters[0] == "r" or "R":
        i = 2

    if individualLetters[0] == "k" or "K":
        i = 3

    if individualLetters[0] == "o" or "O":
        i = 4
    
    else:
        print("You must use only the letters m, i, r, k, o!")

    print(i)
    print(line1[i])
    print(line2[i])
    print(line3[i])
    print(line4[i])
    print(line5[i])



if __name__ == "__main__":
    # mainfunc()
    printLetter()