# We create the letters structure here in the order M, I, R, K, O
# line1 = ["## ##", "#####", "#### ", "#   #", " ### "]
# line2 = ["# # #", "  #  ", "#   #", "#  # ", "#   #"]
# line3 = ["# # #", "  #  ", "#### ", "###  ", "#   #"]
# line4 = ["#   #", "  #  ", "#   #", "#  # ", "#   #"]
# line5 = ["#   #", "#####", "#   #", "#   #", " ### "]


letters = input()
    
individualLetters = letters.split()

print(len(individualLetters))

M = ["## ##", "# # #", "# # #", "#   #", "#   #"]
I = ["#####", "  #  ", "  #  ", "  #  ", "#####"]
R = ["#### ", "#   #", "#### ", "#   #", "#   #"]
K = ["#   #", "#  # ", "###  ", "#  # ", "#   #"]
O = [" ### ", "#   #", "#   #", "#   #", " ### "]

def mainfunc(n):
    if individualLetters[n] == "m":
        i = 0
        while i <= 4:
            print(M[i] + " ")
            i += 1
            
    if individualLetters[n] == "i":
        i = 0
        while i <= 4:
            print(I[i] + " ")
            i += 1
    else:
        print("You must use only the letters m, i, r, k, o!")
    

# def printLetter(letter):
#     i = 5

#     if individualLetters[letter] == "m":
#         print()
#         i = 0

#     if individualLetters[letter] == "i":
#         i = 1

#     if individualLetters[letter] == "r":
#         i = 2

#     if individualLetters[letter] == "k":
#         i = 3

#     if individualLetters[letter] == "o":
#         i = 4
    
    

#     print(i)
#     print(line1[i])
#     print(line2[i])
#     print(line3[i])
#     print(line4[i])
#     print(line5[i])



if __name__ == "__main__":
    n = 0
    while n <= len(individualLetters):
        mainfunc(n)
        n += 1