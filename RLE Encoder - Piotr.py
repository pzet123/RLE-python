#RLE encoder By Piotr, 12Kol
import time

def encodeString(stringToEncode):
    words = stringToEncode.split(" ")
    encodedString = ""
    for word in words: #Goes through each word in the string provided
        if(len(word) > 1):
            nextLetter = word[1]
        newWord = ""
        currentPos = 0
        startingPos = 0
        endingPos = 0
        repeated = False 
        for letter in word: # Goes through each letter in the word provided
            try: #Try and except statement in place to avoid errors when getting to the last letter where the index plus 1 would be out of range 
                nextLetter = word[currentPos + 1]
            except:
                nextLetter = currentPos
            if(letter == nextLetter and not repeated): # Checks if the next letter is the same as the current and if the previous letter isn't the same
                startingPos = currentPos #Used to determine where the repetition started
                repeated = True #Used to show that the current letters are repeating
            elif(letter != nextLetter and repeated): #Used to check if the repititon has stopped
                endingPos = currentPos
                amountOfRepeatedLetters = ((endingPos - startingPos) + 1)
                newWord += ("¬" + str(amountOfRepeatedLetters) + letter) #Converts the repeated letters to the form of "¬ amountOfTimesRepeated letter"
                startingPos = 0
                endingPos = 0
                repeated = False
            elif(letter != nextLetter):
                newWord += letter


            currentPos += 1
        encodedString += (newWord + " ") #Adds each encoded word to the new encoded string
    print(encodedString)
    
            



stringInput = input("Enter a string to encode, only repetitions of two or more " +
                    "continuous letters are encoded, for example 'heeeeello' or 'aaaaaa'")

encodeString(stringInput)
time.sleep(10)

