import random
def guess_no():
    num = random.randint(0,99)
    user_attempt = 0
    allowed_attempt = 5
    while user_attempt < allowed_attempt:
        print(f"{allowed_attempt}-{user_attempt}")
        user_attempt+=1
        guess = (int(input("enter your guess:")))
        print(guess)
        if user_attempt >= allowed_attempt:
            print("you lost")
            break
        if guess == num:
            print("congrates your guess is correct")
            break
        elif guess< num:
            print("your guess is too low")
        elif guess > num:
            print("your guess is too high")
        else: 
            print("invalid input")
            
guess_no()
