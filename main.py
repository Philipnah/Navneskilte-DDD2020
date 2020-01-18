

# We create the letters structure here in the order M, I, R, K, O
line1 = ["## ##", "#####", "####", "#   #", " ### "]
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

    i = 0
    while i <= 4:
        print("\n" + line2[i] + " ", end="")
        i += 1

    i = 0
    while i <= 4:
        print("\n" + line3[i] + " ", end="")
        i += 1

    i = 0
    while i <= 4:
        print("\n" + line4[i] + " ", end="")
        i += 1

    i = 0
    while i <= 4:
        print("\n" + line5[i] + " ", end="")
        i += 1


if __name__ == "__main__":
    mainfunc()