# importing random module as name r to use randint function
import random as r
num = r.randint(1,10)

user_concent=input("Want to play?")
print()

if user_concent.lower()=="yes":

    # giving player 3 chances to guess
    for i in range(1,4):
        userans = int(input("Number guessed by python? "))
        if userans == num:
            print("Guessed in ",i,"times")
            # to give a new line 
            print( )
            # if the player is able to guess then come out of the loop
            break
        
        else:
            if userans > num:
                print("Guess is too high!")
            else:            
                print("Guess is too low!")   
        
    print("Number guessed by python is :",num) 
    print("try your luck again!") 

else:
    print("have nice day!")  
    print()             