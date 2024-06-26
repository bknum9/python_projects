import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    
    
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        print(guess)
        
        if guess < random_number:
            print('Guess again. Too low')
        elif guess > random_number:
            print('Guess again. Too high')
            
    print('You guessed the number correctly')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print('The computer guessed correctly')
    
computer_guess(100)