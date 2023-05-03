import random

print('Hello, What is your name')
name = input()

print('Cool, ' + name + ' I have selected a number between 1 and 20')
secretNumber = random.randint(1, 20)


def takeGuess():
    try:
        for numberOfGuesses in range(1, 7):
            print('Take a guess')
            guess = int(input())

            if (guess < secretNumber):
                print('Your guess is too low')
            elif (guess > secretNumber):
                print('Your guess is too high')
            else:
                break
        if guess == secretNumber:
            print('Yes, you guessed it right in ' +
                  str(numberOfGuesses) + ' attempts ' + name)
        else:
            print("You took too many attempts. The secretNumber was " +
                  str(secretNumber))
    except:
        ValueError
        print('Please enter guess only in integers')


takeGuess()
