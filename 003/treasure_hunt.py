#Treasure hunt Game
#GO -> Game Over
#Right -> Go
#Left -> Ok
#Swim -> GO
#wait -> OK
#Door Yellow -> OK
#Door Blue -> GO
#Door Red -> Go
print("Welcome to the best treasure hunt game!!!\n")
print("Enter X to end game.\n\n")
user_choice = input("Select if you would like to go Right or Left, enter R for right or L for Left: ")
if user_choice.lower() == "X" or user_choice.lower() == "":
    print("Thank you for playing!")
elif user_choice.lower() == "l":
    user_choice = input("You have arrived at an island select if you would like to wait or swim, enter S for swim or W for wait: ")
    if user_choice.lower() == "w":
        user_choice = input("You are safe, select door to continue, enter R for Red, Y for Yellow or B for Blue: ")
        if user_choice.lower() == "y":
            print("You win !!!")
        else:
            print("Game Over !!!")
    else:
        print("Game Over !!!")
else:
    print("Game Over !!!")


#TODO:Refactor to use functions and while loop

    

