# IPND Stage 2 Final Project

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/

content = ""
difficulty = ""
study_words = []
study_paragraph = ""


def set_difficulty():
    attempt = 0
    while True:
        if attempt == 0:            
            difficulty = raw_input("Please enter the difficulty of the Fill-in-the-Blanks paragraph you would like to try (easy, medium or hard): ")
            if difficulty.lower() == "easy" or difficulty.lower() ==  "medium" or difficulty.lower() == "hard":
                return difficulty
        else:
            difficulty = raw_input("Attempt #" + str(attempt) + ": Please try again by entering \"easy\", \"medium\" or \"hard.\"")
            if difficulty.lower() == "easy" or difficulty.lower() ==  "medium" or difficulty.lower() == "hard":
                return difficulty
        attempt += 1    
            

def get_content(difficulty):
    with open("files/" + difficulty + ".txt", "r") as study_file:
        content = study_file.read()
    return content


def set_study_words(paragraph):
    words = []
    words_end = "*****"
    number = 1
    for word in paragraph.split():
        if word == words_end:
            return words
        else:
            words.append([word, number])
            number += 1
    return words
    

def set_up_paragraph(paragraph, study_words):
    new_paragraph = ""
    paragraph_start = paragraph.find("*****") + 5
    study_paragraph = paragraph[paragraph_start:].split()
    replacement_word_start = 0
    replacement_word_end = 0

    for string in study_paragraph:
        new_string = ""
        search_term = ""
        for word in study_words:
            search_term = string.lower()
            if search_term.find(word[0]) == -1:
                  new_string = string    
            else:
                  if search_term.find(word[0]) != -1:
                      replacement_word_start = search_term.find(word[0])
                      replacement_word_end = replacement_word_start + len(word[0])
                      new_string = string.replace(string[replacement_word_start:replacement_word_end], "___" + str(word[1]) + "___")
                      break
        new_paragraph += new_string + " "
    return new_paragraph
    

def set_up_board(difficulty, study_paragraph, study_words):
    print "\n\nYou have chosen the \"" + difficulty + "\" level of difficulty."
    print "\nYou will get 5 guesses per problem."
    print "\nThe current paragraph reads as:"
    print study_paragraph 
    
    if difficulty == "easy":
        print "\nPossible words:\n--------------------------"
        for word in study_words[::-1]:
            print word[0],
        print "\n--------------------------"
    if difficulty == "medium":
        print "\nPossible words (masked):\n--------------------------"
        for word in study_words[::-1]:
            print " ",
            for char in word[0]:
                print "*",
        print "\n--------------------------"
    if difficulty == "hard":
        print "\n--------------------------\nNo clues on \"hard\" difficulty.  :)"
        

def fill_answers(paragraph, word):
    paragraph = paragraph.replace("___" + str(word[1]) + "___", word[0])
    return paragraph

    
def get_user_answers(paragraph, study_words):
    if study_words == []:
        print "Congratulations!  You got them all right!"
        quit()
    for word in study_words:
        tries = 0
        while tries < 5:
            answer = raw_input("\n\nWhat would be the replacement for ___" + str(word[1]) + "___? ==> ")
            if answer.lower() == word[0]:
                print "Correct!\n"
                paragraph = fill_answers(paragraph, word)
                print paragraph
                study_words.remove(word)
                get_user_answers(paragraph, study_words)
            tries += 1
        quit()
    

def do_exercise(paragraph, difficulty):
    difficulty = set_difficulty()
    paragraph = get_content(difficulty)
    study_words = set_study_words (paragraph)
    study_paragraph = set_up_paragraph(paragraph, study_words)
    set_up_board(difficulty, study_paragraph, study_words)
    get_user_answers(study_paragraph, study_words)
    


do_exercise(content, difficulty)



# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well

      #sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
      #adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
      #don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
      #tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/  
