import random

# Starts the loop 
while True:
    user_action = input("Enter your choice(R for rock, P for paper, S for scissors)")
    options = ['R','P','S']
    comp_action = random.choice (options)
    
#checks if the user's choice is in the option
    if user_action not in options:
            print('Invalid choice, Try again\n')
            continue
            
    else:
            print(f"\nYou chose {user_action}, computer chose {comp_action}.\n")
            if user_action == comp_action:
                print(f"Both players selected {user_action}. It's a tie!")
            elif user_action == 'R':
                if comp_action == 'S':
                    print("Rock smashes scissors! You win!")
                else:
                    print("Paper covers rock! You lose.")
            elif user_action == 'P':
                if comp_action == 'R':
                     print("Paper covers rock! You win!")
                else: 
                     print("Scissors cuts paper! You lose.")
            elif user_action == 'S':
                if comp_action == 'P':
                    print("Scissors cuts paper! You win!")
                else:
                     print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break


    # if user_action == comp_action:
    #     print(f"Both players selected {user_action}. It's a tie!")
    # elif user_action == "R":
    #     if comp_action == "S":
    #         print("Rock smashes scissors! You win!")
    #     else:
    #         print("Paper covers rock! You lose.")
    # elif user_action == "P":
    #     if comp_action == "R":
    #         print("Paper covers rock! You win!")
    #     else:
    #         print("Scissors cuts paper! You lose.")
    # elif user_action == "S":
    #     if comp_action == "P":
    #         print("Scissors cuts paper! You win!")
    #     else:
    #         print("Rock smashes scissors! You lose.")

    # play_again = input("Play again? (y/n): ")
    # if play_again.lower() != "y":
    #     break

 