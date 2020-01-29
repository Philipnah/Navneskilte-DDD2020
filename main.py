# We create the letters structure here in the order M, I, R, K, O
# line1 = ["## ##", "#####", "#### ", "#   #", " ### "]
# line2 = ["# # #", "  #  ", "#   #", "#  # ", "#   #"]
# line3 = ["# # #", "  #  ", "#### ", "###  ", "#   #"]
# line4 = ["#   #", "  #  ", "#   #", "#  # ", "#   #"]
# line5 = ["#   #", "#####", "#   #", "#   #", " ### "]


letters = input().lower()

def split(word): 
    return [char for char in word]
    
individualLetters = split(letters)

print("\n")

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

    if individualLetters[n] == "r":
        i = 0
        while i <= 4:
            print(R[i] + " ")
            i += 1

    if individualLetters[n] == "k":
        i = 0
        while i <= 4:
            print(K[i] + " ")
            i += 1

    if individualLetters[n] == "o":
        i = 0
        while i <= 4:
            print(O[i] + " ")
            i += 1

    else:
        print("\nYou must use only the letters m, i, r, k, o!\n")



if __name__ == "__main__":
    n = 0
    while n <= len(individualLetters):
        mainfunc(n)
        n += 1