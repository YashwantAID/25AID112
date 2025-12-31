##Number guessing game (simple version):Secret number = 7..
##Let user guess (use while loop) until they guess correctly. After each wrong guess print "Too high" or "Too low".

secret_number = 7
guess = int(input("Guess the secret number : "))
while guess != secret_number:
    
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:   
        print("Congratulations! You guessed it right.")
    guess = int(input("Guess the secret number : "))

print("Congratulations! You guessed it right.")

