import random
def play():
    num = random.randrange(0,21)
    name = input("Hello! What is your name?\n")
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')
    num_guesses = 0
    guess = None
    while guess != num:
        num_guesses += 1
        e_raised = True
        while e_raised:
            try:
                guess = int(input('Take a guess.\n'))
            except:
                print('Please enter a number.')
            else:
                e_raised = False
        if guess < num:
            print('Your guess is too low.')
        elif guess > num:
            print('Your guess is too high')
        else:
            print(f'Good job {name}! You guessed the number in {num_guesses} guesses!')

play()
    
