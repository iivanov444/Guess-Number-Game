import random, time

def play_game(user_attempts, random_choice) -> None:
    while True:
        if user_attempts == 0:
            print(f"No attempts left! The number was: {random_choice}")
            time.sleep(3)
            break

        print(f"Attempts left: {user_attempts}")

        player_choice = 0

        try:
            player_choice_input = input()

            if player_choice_input == "":
                print("No input detected. Exiting the game.")
                break

            player_choice = int(player_choice_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            user_attempts -= 1
            continue

        if player_choice not in range(0, 101):
            print("Invalid: Number out of range.")
        else:
            if random_choice == player_choice:
                print("You guessed it!")
                break
            elif random_choice > player_choice:
                print("Too low!")
            elif random_choice < player_choice:
                print("Too high!")

        user_attempts -= 1

def get_user_attempts() -> int:
    while True:
        try:
            user_attempts_input = input("Choose how many attempts you need from 1 to 10: ")
            
            if user_attempts_input == "":
                print("No input detected. Exiting the game.")
                raise SystemExit
            
            user_attempts = int(user_attempts_input)
            if user_attempts not in range(1, 11):
                raise ValueError("Invalid attempts amount. Please enter from 1 to 10.")
            
            return user_attempts

        except ValueError as e:
            print(e)

def main():
    random_choice = random.randint(0, 100)
    
    user_attempts = get_user_attempts()

    print("Guess a number from 0 to 100: ")
    
    play_game(user_attempts, random_choice)

    raise SystemExit

if __name__ == '__main__':
    main()