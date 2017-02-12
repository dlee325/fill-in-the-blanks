# Fill-in-the-blanks Quiz
# Ask user for difficulty level.
# Prompt a user with a sentence (based on difficulty) containing several blanks.
# User should then be asked to fill in each blank appropriately to complete the sentence.

# Inputs for difficulty levels
difficulty_list = ['easy', 'medium', 'hard']

# Inputs for answers
answers = []
blanks  = ["___1___", "___2___", "___3___", "___4___"]
easy_answers = ["function", "parameters", "None", "lists"]
medium_answers = ["pwd", "ls", "open", "cd"]
hard_answers = ["mutation", "Aliasing", "append", "len"]

# Inputs for quizzes
quiz = ""
easy_quiz = "A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions."
medium_quiz = "In a command line interface CLI, ___1___ tells you where you are in the directory, ___2___ lists directories and files inside a given directory, ___3___ opens a directory, and ___4___ changes the directory, allowing you to travel to another directory."
hard_quiz = "Supported by lists but not strings, ___1___ changes the value of an object. ___2___ is when there are two names that refer to the same object. The ___3___ method adds a new element to the end of a list. The ___4___ operator can be used to find out the length of an object."


def difficulty(list):
	level = ""
	user_difficulty = raw_input("Please select a game difficulty by typing it in! Possible choices include easy, medium, and hard:\n\n")
	if user_difficulty in list:
		level += user_difficulty
		return level

def answers(level):
	answers = []
	if level == "easy":
		answers += easy_answers
	elif level == "medium":
		answers += medium_answers
	elif level == "hard":
		answers += hard_answers
	return answers
		
def display_quiz(string): # Determines what quiz to display
	if string == 'easy': # Display the quiz based on what difficulty user chose
		return easy_quiz
	elif string == 'medium':
		return medium_quiz
	return hard_quiz

def fill_in(word, blanks):
	for e in blanks:
		if e in word:
			return e
	return None


def check_answers(level, answers, quiz): # Presents quiz and asks user for answer and checks if it's correct.
	print "\nYou've chosen " + level + "!\n\nYou will get 5 guesses per problem. \n\nThe current paragraph reads as such:\n\n" + quiz
	index  = 0
	total_blanks = len(blanks)
	max_attempts = 5
	last_question = 3
	while index < total_blanks:
		attempts = 0
		while attempts < max_attempts:
			user_answer = raw_input("\nWhat should be substituted for" + blanks[index] + "?\n\n")
			if user_answer == answers[index]:
				print "\nCorrect!\n"
				quiz = quiz.replace(blanks[index], answers[index])
				print quiz
				if index == last_question:
					quit("\nYou win!")
				attempts += max_attempts
			else:
				attempts += 1
				if attempts == max_attempts:
					quit("\nThat isn't the correct answer! You have 0 tries left! You Lose!")
				print "\nThat isn't the correct answer! Let's try again; you have " + str(5 - attempts) + " tries left!"
		index += 1

def run_quiz(quiz, answers, difficulty_list):
	level = difficulty(difficulty_list) # Run difficulty function
	answers = answers(level) # Calls answers based on difficulty
	quiz = display_quiz(level)
	check_answers(level, answers, quiz)

print run_quiz(quiz, answers, difficulty_list)