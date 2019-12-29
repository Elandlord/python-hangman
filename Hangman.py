import random
import os

class HangMan:
    wordToGuess = ""
    maxErrors = 0
    wordList = list()
    
    errorsMade = 0
    gameWon = 0
    guessedLetters = list()
    correctLetters = list()
    
    options = {
        "1": "Guess a letter",
        "2": "Guess the word",
    }
    
    def __init__(self, wordToGuess, maxErrors):
        self.wordToGuess = wordToGuess.lower()
        self.maxErrors = maxErrors
        self.wordList = list(self.wordToGuess)
        for i in self.wordList[0:(len(self.wordList))]:
            self.correctLetters.append("_")
        
    def startGame(self):
        self.printWelcomeMessage()
        
        while(self.errorsMade <= self.maxErrors and not self.wordIsGuessed()):
            self.cls()
            self.showError()
            print(*self.correctLetters)
            self.printNewLines()
            selectedOption = self.chooseOption()
            
            if(selectedOption == "1"):
                self.nextLetter()
                
            if(selectedOption == "2"):
                self.guessWord()

        if(self.wordIsGuessed() or self.gameWon == 1):
            self.printNewLines()
            print("Winner winner chicken dinner!")
            self.printNewLines()
            
        if(self.errorsMade > self.maxErrors):
            self.printNewLines()
            print("You met your untimely demise.")
            self.printNewLines()
        
    def nextLetter(self):
        letter = input("Guess a letter:", ).lower()
        
        if(len(letter) > 1):
            print("Don't try to fuck with the system by putting too many characters")
        
        if(self.letterWasGuessedBefore(letter)):
            print ("Letter was guessed before. Try again with a different letter.")
            return
            
        self.guessLetter(letter)
        
    def guessLetter(self, letter):
        self.guessedLetters.insert(-1, letter)
        
        if(letter in self.wordList):
            duplicates = [i for i, x in enumerate(self.wordList) if x == letter]
                
            for duplicate in duplicates:
                del self.correctLetters[duplicate]
                self.correctLetters.insert(duplicate, letter)
            
            print("Good guess!")
            self.printNewLines()
            return
            
        self.incrementError()
        
    def chooseOption(self):
        for option in self.options:
            print(str(option) + ": " + self.options[option])
            
        self.printNewLines()
        choice = input("Choose option by typing the correct number: ", )
        self.printNewLines()
        
        if(str(choice) not in self.options):
            self.chooseOption()
            
        return choice
        
    def showError(self):
        print("Errors made: " + str(self.errorsMade))
        
    def incrementError(self):
        self.errorsMade += 1
        self.printNewLines()
        print("You guessed wrong! Errors made: " + str(self.errorsMade))
        self.printNewLines()
        
    def guessWord(self):
        guessedWord = input("Guess your word: ", )
    
        if(guessedWord.lower() == self.wordToGuess):
            self.gameWon = 1
            return
        self.incrementError()
            
        
    def letterWasGuessedBefore(self, letter):
        return (letter in self.guessedLetters)
        
    def wordIsGuessed(self):
        return all(letter in self.correctLetters for letter in self.wordList) or self.gameWon
        
    def printWelcomeMessage(self):
        welcomeText = """
            Let's play Hangman!
            
            The word you have to guess, contains {0} characters.
            The maximum amount of errors allowed, is {1}.
        """;
        
        print(welcomeText.format(len(self.wordList), self.maxErrors))
        
        self.printNewLines()
        
    def printNewLines(self, amount=1):
        for i in range(amount):
            print("\n")
            
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')
        
dict = {
    1:"sausage",
    2:"klaasmeister",
    3:"elandlord",
    4:"ageofempiresrules",
    5:"bacon",
}
hangman = HangMan(dict[random.randint(1,len(dict))], 5);
hangman.startGame()
        
    
