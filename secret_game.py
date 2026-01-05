import random



secret_number = random.randint(1,50)

game_play = True

while game_play:
    guess = int(input("I'm thinking of a number between 1 and 50. Can you guess it?: "))

    match guess:
        case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
            
        case _ if guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
            
        case _:
            print("Congratulations, you guessed it!")
            
            break
        
        
        
        
            

        
        
    