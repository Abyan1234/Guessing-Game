import random
print("Number Guessing Game")
number=random.randint(1,9)
chances=0
print("Guess a Number(Between 1 and 9)")
while chances < 5:
    guess=int(input("Enter Your Guess:- "))
    
    if guess==number:
        print("Congradulations You Won")
        break
    elif  guess<number:
        print("Your guess was too Low: guess a number higher than",guess)
        
        break
    else:
        print("Your guess was too high: guess a number lower than",guess)

    chances+=1

    if not chances<5:
        print("You Lose!!! The Number is",number)    