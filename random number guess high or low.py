import random
hidden =random.randint(1,20)
enterd_num = int(input("Guess the number(Between 1 & 20 :"))
if enterd_num == hidden:
    print("you guess the correct the number ")
else:
    while enterd_num != hidden:
        if enterd_num> hidden:
            print("Guess the number too high")
        elif enterd_num< hidden:
            print("Guess the number too low")
        print("Please guess  again")
        enterd_num = int(input("Guess the number(Between 1 & 20 :"))
    print(("you guess the correct the number "))


