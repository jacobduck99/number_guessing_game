import random

def number_guessing():

    print("Welcome to the Number Guessing Game!")
    print("Type 'quit' at any time to exit.")
    random_num = random.randint(1, 100)
    player_counter = 0
    attempts = 0

    while True: 
        user_guess = input("Enter your guess (1-100): ").lower()
        user_input = int(user_guess)

        if user_input == "quit":
            print("Goodbye!")
            exit()  

        if user_input  == random_num:
            print(f"🎉 You win the guess {user_input} was correct!")
            player_counter += 1
            attempts += 1
            break
        elif user_input > random_num:
            print(f"Your guess of {user_input} is too high!")
            attempts += 1
        
        else:
            print(f"Your guess {user_input} is too low!")
            attempts += 1
        

            
        
    print(f"\nYou got {player_counter} correct out of {attempts} attempts.")
        

number_guessing()