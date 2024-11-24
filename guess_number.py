import random



def guess_number(): 
    target = random.randint(1, 100)
    life = 3
    while life >0:
        guess=int(input("enter number: "))
        if guess < target:
            life-=1
            print( "Too low! Try again.")
        elif guess > target: 
            life -=1   
            print("Too high! Try again.")
        else:
           print("Congratulations! You guessed the correct number.")

guess_number( )