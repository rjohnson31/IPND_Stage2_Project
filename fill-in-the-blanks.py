'''
PROGRAM: fill-in-the-blanks.py
PURPOSE: This program takes user input regarding difficulty of the exercise and
	the number of guesses available to the user.  It then reads the appropriate file
	based on the difficulty chosen, sets up the study words and the passage(s).  
	Depending on the difficulty, it may display hints under the passage(s).  It then
	queries the user for appropriate answers for the fill-in-the-blanks.  As the 
	user inputs the correct answers, the word is placed into the passage(s) and 
	the user is prompted for the next answer until the maximum number of attempts
	is reached or all of the answers are successfully completed.
AUTHOR: CJ
DATE: 11Aug16
COURSE: IPND - Stage 2 Project 
'''

content = ""
difficulty = ""
max_attempts = 0
study_words = []
study_paragraph = ""


#set_difficulty() prompts the user for the desired difficulty.  The response is returned and 
#   used both to point to the appropriate file to open for content and to adjust the 
#   level of hints displayed on the board.
#TODO:  Implement changes to have filenames (topics) to be chosen to set the appropriate
#   file to use.  Difficulty should only affect the hints given, not content.
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

#set_max_attempts() prompts user for max attempts from 1 to 10.  Return initiates
#  a default value of 5.
#TODO:  Consolidate with set_difficulty() so that the user is prompted once for both values.
def set_max_attempts():
    attempt, min_attempts, max_attempts, default_attempts = 0, 1, 10, 5 
    while True:
        if attempt == 0:            
            user_input = raw_input("What is the maximum number of attempts you want to try for each question (1-10; return for default = 5): ")
            if user_input == '':
                user_input = default_attempts 
                return user_input
            if min_attempts <= int(user_input) <= max_attempts:
                user_input = int(user_input) 
                return user_input
        attempt += 1 
            
#get_content() opens a file based on the difficulty chosen and reads in the contents
#  for processing by set_up_paragraph() and set_study_words.
#TODO:  Change this area to display folder "files/" contents and prompt user for choice
#  of "topic" they would like to study.
def get_content(difficulty):
    with open("files/" + difficulty + ".txt", "r") as study_file:
        content = study_file.read()
    return content

#set_study_word() gleens the words at the top of the content and creates a list of the
#  word and an incremented number.  Both used when replacing the words and indicating
#  within the paragraph where that word goes.
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
    
#set_up_paragraph() takes the main paragraph(s), identifies and replaces all instances
#  of a study word with the requisite blanks and its associated number (___1___).
#TODO:  Capitalization is lost.  Misses rare instances of words (e.g., "-study_word")
#  Paragraph/Line formatting is lost.  Flash-card functionality is a thought, too.
def set_up_paragraph(paragraph, study_words):
    new_paragraph, paragraph_start = "", paragraph.find("*****") + 5 
    # 5 is the length of the arbitrarily designated separator "*****"
    # Since the feeder files are editable insofar as study words and paragraph, 
    # a clear separator was required.  This code breaks down without it or with multiple in the file. 
    study_paragraph = paragraph[paragraph_start:].split()
    replacement_word_start = replacement_word_end = 0
    for string in study_paragraph:
        new_string = search_term = ""
        for word in study_words:
            if string.lower().find(word[0]) == -1:
                new_string = string    
            elif string.lower().find(word[0]) != -1:
                replacement_word_start = string.lower().find(word[0])
                replacement_word_end = replacement_word_start + len(word[0])
                new_string = string.replace(string[replacement_word_start:replacement_word_end], "___" + str(word[1]) + "___")
                break
        new_paragraph += new_string + " "
    return new_paragraph
    
#set_up_board() displays the full board to the user.
#TODO:  Hints area shows only on initial display.  Except for "hard," it should 
#  show for each display and the hint word display should update according to the 
#  correct responses.  Randomize words for hint display.   
def set_up_board(difficulty, study_paragraph, study_words, max_attempts):
    print "\n\nYou have chosen the \"" + difficulty + "\" level of difficulty."
    print "\nYou will get " + str(max_attempts) + " guesses per problem."
    print "\nThe current paragraph reads as:"
    print study_paragraph  
    if difficulty == "easy":
        print "\nPossible words:\n--------------------------"
        for word in study_words[::-1]:
            print word[0],
    if difficulty == "medium":
        print "\nPossible words (masked):\n--------------------------"
        for word in study_words[::-1]:
            print " ",
            for char in word[0]:
                print "*",
    if difficulty == "hard":
        print "\n--------------------------\nNo clues on \"hard\" difficulty.  :)"
        
#get_user_answers() prompts user for answers, tracks progress and initiates paragraph
#  word replacement on correct responses.  Quits program when max_attempts or complete.
#TODO:  Implement sleep delay before quit().    
def get_user_answers(paragraph, study_words, max_attempts):
    if study_words == []:
        print "Congratulations!  You got them all right!"
        quit()
    for word in study_words:
        tries = 1
        while tries <= max_attempts:
            answer = raw_input("\n\nWhat would be the replacement for ___" 
            	+ str(word[1]) + "___? Try " + str(tries) + " of " 
            	+ str(max_attempts) + ":  " )
            if answer.lower() == word[0]:
                print "Correct!\n"
                paragraph = fill_answers(paragraph, word)
                print paragraph
                study_words.remove(word)
                get_user_answers(paragraph, study_words, max_attempts)
            tries += 1
        quit()

#fill_answers() replaces the blanks and number with the appropriate word on correct responses.
#TODO:  Capitalization not maintained.
def fill_answers(paragraph, word):
    filled_in_paragraph = paragraph.replace("___" + str(word[1]) + "___", word[0])
    return filled_in_paragraph
    
#do_exercise() initializes primary program procedures and variables.
def do_exercise(paragraph, difficulty, max_attempts):
    difficulty = set_difficulty()
    max_attempts = set_max_attempts()
    paragraph = get_content(difficulty)
    study_words = set_study_words (paragraph)
    study_paragraph = set_up_paragraph(paragraph, study_words)
    set_up_board(difficulty, study_paragraph, study_words, max_attempts)
    get_user_answers(study_paragraph, study_words, max_attempts)
    

#do_exercise() - initialization call.
do_exercise(content, difficulty, max_attempts)
