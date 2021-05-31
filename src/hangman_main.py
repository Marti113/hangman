#Main page for the program, calls and handles user input

#Generate a random, secret word (using WordsAPI ideally)
#Need some user interface to show the user the length of the word
#Need to accept single letter user input
#Letter checker, checks if the user given letter is in the word
#If the letter is in the word-- add the letter to the secret word string ex "---e---"
#If the letter is NOT in the word, letter is added to was_guessed set, the user is informed they were wrong, and
#the Hangman is one line closer to being complete
#Two final outcomes:
#1: User guesses the word (they win)
#2: The hangman drawing is complete, user loses, word is revealed

class Hangman:

    def __init__(self, guessed_letters):
        #generate random word here using Words API
        self.secret_word = "test"
        self.guess_template = len(self.secret_word)*"_"
        self.guessed_letters = guessed_letters
        self.count = 0
        self.game_over = False

    def start_game(self):
        secret_word = self.secret_word
        self.guess_template = len(secret_word)*"_"
        return self.guess_template

    def user_guess(self):
        self.count += 1
        guess_letter = input("Guess a letter in the secret word!")
        if not guess_letter.isalpha():
            print("that's not a letter try again!")
            guess_letter = input("This time use a letter a-z")
        if not len(guess_letter) == 1:
            guess_letter = input("guess one letter a turn! Try again")
        return guess_letter.lower()

    #helper function for game play, returns True is the guess is correct, False if it's wrong
    #should be used so the True or False return prompts the user about their guess (right or wrong)
    #right guess == updated guess word ---- wrong guess == guessed word array
    def letter_check(self, a_letter):
        guess = self.guess_template
        guessed_letters = self.guessed_letters
        secret_word = self.secret_word

        if a_letter in secret_word:
            #do letter reveal logic here
            for i in range(len(secret_word)):
                if secret_word[i] == a_letter:
                    #why does guess not save updated with the new, correct letter?
                    guess = guess[:i] + a_letter + guess[i+1:]
                    self.guess_template = guess

            return "You got a letter right, the word now looks like: " + guess
        else:
            guessed_letters.append(a_letter)
            print(guessed_letters)
            return "Welp, you guessed wrong, here are a list of your previously guessed letters: " + str(guessed_letters)

    def win_check(self):
        guess = self.guess_template
        secret_word = self.secret_word
        if guess == secret_word and self.count <= len(secret_word):
            return True
        else:
            return False

    #keeps track of the number of user guesses
    def hangman_count(self):
        secret_word = self.secret_word
        if self.count == len(secret_word):
            return True
        else:
            return False

    def draw_hangman(self):
        hang_man = {1:'/', 2: '/\\', 3: '|'
                                        '/\\'}
        return hang_man[self.count]

test_game = Hangman([])

print(test_game.start_game())
#guessed_letter = test_game.user_guess()
#print(test_game.letter_check(guessed_letter))
while not test_game.game_over:
    guessed_letter = test_game.user_guess()
    print(test_game.letter_check(guessed_letter))
    print(test_game.draw_hangman())
    if test_game.win_check():
        print("You won congrats!")
        test_game.game_over = True
    elif test_game.hangman_count():
        print("You lost, try again!")
        test_game.game_over = True

