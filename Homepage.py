import random


def Number_Game():
    
    print("Welcome to the number game!")
    
    score = 0
    
    top_of_range = int(input("Type a number: "))
    
    random_number = random.randint(1, top_of_range)
    
    guessed_number = int(input(f"Geuss the number between 0 and {top_of_range}: "))
    
    if guessed_number == random_number:
        print("You guessed the number!")
        score += 1
    else:
        print("That isn't the number!")
    
    print(f"You guessed {str(score)} number/s correctly.")


def Rockpaper():
    score = 0
    print("Welcome to rock paper scissors!")
    def play():
        player = input("Player Choice: ").lower()
        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)
        print(f"Computer Choice: {computer}")
        if player == "rock" and computer == "scissors":
            print("Rock beats scissors. You win!")
            score += 1
        elif player == "paper" and computer == "rock":
            print("Paper beats rock. You win!")
            score += 1
        elif player == "scissors" and computer == "paper":
            print("Scissors beats paper. You win!")
            score += 1
        elif player != choices:
            print("You made a spelling mistake. Minus one point.")
            score -= 1
        else:
            print("The computer beat you!")
    play()
    play()
    play()
    print(f"You won {score}/3 rounds!")


def Quiz():
    print("Welcome to Ethan's computer quiz!")
    
    playing = input("Do you want to play? ")
    
    if playing.lower() != "yes":
        quit()
    
    print("Okay! Let's play! :)")
    score = 0
    
    answer = input("What does html stand for? ")
    if answer.lower() == "hypertext markup language":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    
    answer = input("Can you use Python for AI? ")
    if answer.lower() == "yes":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        
    answer = input("Who owns VS Code? ")
    if answer.lower() == "microsoft":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        
    answer = input("Who made Apple? ")
    if answer.lower() == "steve jobs":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        
    print(f"you got {str(score)}/4 questions right!")
    print(f"you got {str(score / 4 * 100)}%")


def Age():
    print("Welcome to the age calculator")
    current_year = input("what year is it? ")
    birth_year = input("enter your birth year: ")
    age = int(current_year) - int(birth_year)
    print(f"you are {age} years old")


def Time():
    print("Welcome to the time calculator!")
    days = int(input("Number of days: "))
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    milliseconds = seconds * 60
    print(f"Number of hours: {hours}")
    print(f"Number of minutes: {minutes}")
    print(f"Number of seconds: {seconds}")
    print(f"Number of milliseconds: {milliseconds}")


def Norm():
    print("Welcome to the normal calculator!")

    operation = input("what operation do you want to use? ")

    if(operation == "addition"):
        num1 = float(input("First: "))
        num2 = float(input("Second: "))
        Sum = num1 + num2
        print(f"Sum: {Sum}")
    elif(operation == "subtraction"):
        num1 = float(input("First: "))
        num2 = float(input("Second: "))
        Sum = num1 - num2
        print(f"Sum: {Sum}")
    elif(operation == "multiplication"):
        num1 = float(input("First: "))
        num2 = float(input("Second: "))
        Sum = num1 * num2
        print(f"Sum: {Sum}")
    elif(operation == "division"):
        num1 = float(input("First: "))
        num2 = float(input("Second: "))
        Sum = num1 / num2
        print(f"Sum: {Sum}")
    else:
        print("This operation does not exist. Try checking your spelling.")


line01 = "********************"
line02 = "*                  *"
line03 = "*     WELCOME!     *"

print("")
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)

while True:
    app = input("Would you like to play a game or use a calculator? Press q to quit. ").lower()
    if app == "game":
        game_mode = input("What game do you want to play? (Number Game, Quiz Game, rock paper scissors) ").lower()
        if game_mode == "number game":
            Number_Game()
        elif game_mode == "quiz game":
            Quiz()
        elif game_mode == "rock paper scissors":
            Rockpaper()
    elif app == "calculator":
        calc_mode = input("What calculator do you want to use? (Normal Calculator, Age Calculator, Time Calculator) ").lower()
        if calc_mode == "normal calculator":
            Norm()
        elif calc_mode == "age calculator":
            Age()
        elif calc_mode == "time calculator":
            Time()
    elif app == "q":
        quit()
    elif app == "a":
        print("404 not found")
    elif app == "swifty":
        print("[ERROR_ACCESS_DENIED (0x5)]")
        quit(2)
    elif app == "fun":
        fun()
    else:
        print("You may have made a spelling error. Try again.")