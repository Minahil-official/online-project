from abc import ABC, abstractmethod
import random

class Games(ABC):
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
    
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def is_over(self):
        pass

class High_low(Games):
    def __init__(self, player_name):
        super().__init__(player_name)  # Calls the parent class initializer
        self.count = 0
        self.score = 0
    
    def play(self):
        while self.count < 3:
            self.count += 1
            self.comp_num = random.randint(1, 100)
            self.my_num = random.randint(1, 100)
            print('Your number is:', self.my_num)
            
            guess = input("Guess whether your number is 'higher' or 'lower' than the computer's number: ")
            print('Computer number is:', self.comp_num)
            
            if guess == 'higher' and self.my_num > self.comp_num:
                print('You are right!')
                self.score += 1
            elif guess == 'lower' and self.my_num < self.comp_num:
                print('You are right!')
                self.score += 1
            else:
                print('You are wrong')
            
            print(f"{self.player_name}, your score is:", self.score)
        
        print('Thanks for playing')
        print('Good job! You played very well')
    
    def is_over(self):
        return self.count >= 3

class GuessNumber(Games):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.user_attempt = 0
        self.allowed_attempt = 5
        self.game_over = False
    
    def play(self):
        num = random.randint(0, 49)
        while self.user_attempt < self.allowed_attempt and not self.game_over:
            print(f"Attempt {self.user_attempt + 1} of {self.allowed_attempt}")
            try:
                guess = int(input("Enter your guess (below 50): "))
                
                if guess >= 50:
                    print("Your guess should be below 50. Try again.")
                    continue

                self.user_attempt += 1
                
                if guess == num:
                    print("Congratulations, your guess is correct!")
                    self.game_over = True
                elif guess < num:
                    print(f"{self.player_name}, your guess is too low.")
                elif guess > num:
                    print(f"{self.player_name}, your guess is too high.")
                
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
            
            if self.user_attempt >= self.allowed_attempt and not self.game_over:
                print(f"{self.player_name}, you lost. The correct number was {num}.")
                self.game_over = True
    
    def is_over(self):
        return self.game_over

class Choose_game:
    def __init__(self):
        pass
    
    @staticmethod
    def game_choice():
        print("Welcome to the Game Engine!")
        print("1. High Low Game")
        print("2. Guess the Number Game")
        
        choice = input("Please choose a game (1 or 2): ")
        player_name = input("Enter your name: ")
        
        if choice == '1':
            game = High_low(player_name)
            game.play()
        elif choice == '2':
            game = GuessNumber(player_name)
            game.play()
        else:
            print("Invalid choice, please select 1 or 2.")
            Choose_game.game_choice()  # Calls the method again on invalid input

# Start the game engine
Choose_game.game_choice()
