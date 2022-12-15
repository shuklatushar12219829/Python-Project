print("WELCOME 🙏")
import random
def game(comp,user):
    if(comp==user):
        return("Its a tie")

    elif(comp=="P"):
        if(user=="R"):
            return("comp wins🙁")
        elif(user=="S"):
            return("user wins😊")

    elif(comp=="R"):
                if(user=="P"):
                    return("user wins😊")
                elif(user=="S"):
                    return("comp wins🙁")

    elif(comp=="S"):
                 if(user=="P"):
                     return("comp wins🙁")
                 elif(user=="R"):
                     return("user wins😊")
i=1
j=int(input("Enter number of rounds you want to play:"))
for d in range(0,j):
    print("Let's play rock(R),paper(P) and scissor(S) game!!!")
    user = input("user's turn rock(R) paper(P) scissor(S) exit(E):")
    if (d == j-1):
        print("End game\nThank You for playing!!!!")
        break
    print("comp's turn rock(R) paper(P) scissor(S):", end="")
    comprand = random.randint(1, 3)
    if (comprand == 1):
        comp = "R"
    elif (comprand == 2):
        comp = "P"
    elif (comprand == 3):
        comp = "S"
    print(comp)
    call = game(comp, user)
    print(call)



