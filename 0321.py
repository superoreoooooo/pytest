import random

"""

age = int(input("age : "))

if (age >= 18) :
    print("pass")
else :
    print("fail")
print("hello")
"""

"""
status = ""

pick = input("my input : ")
pc = random.choice(["rock", "paper", "scissors"])

if (pick == pc) :
    status = "draw"
else :
    if (pick == "rock") :
        if (pc == "paper") :
            status = "win"
        else : 
            status = "lose"
    elif (pick == "paper") :
        if (pc == "rock") :
            status = "win"
        else :
            status = "lose"
    elif (pick == "scissors") :
        if (pc == "paper") :
            status = "win"
        else :
            status = "lose"
    else :
        status = "error"

print("pc input :", pc)
print(status)
"""

hap = 0
s = ""

for i in range (1, 11, 1) :
    hap += i
    if (i == 10) :
        print(i, end = " = ")
    else :
        print(i, end = " + ")
print(hap)