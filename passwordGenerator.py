from random import *
def password():
    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    large = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['!', '#', '$', '%', '&', '(', ')', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '{', '|', '}', '~']
    cho = [small, large, num, special]
    shuffle(cho)
    pswd = []
    for i in cho:
        if i == special:
            temp = sample(i, randint(1, 2))
        else:
            temp = sample(i, randint(3, 4))
        for j in temp:
            pswd.append(j)
    shuffle(pswd)
    return("".join(pswd))
