# IPND Stage 2 Final Project

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
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

easy_quiz = '''___1___ hides in the ___2___.
There are ___3___ ways to write error-free programs; only the ___4___ one works.'''
medium_quiz = '''A ___1___ is defined by default as a ___2___ ___1___ if defined outside of functions.
A ___1___ is ___3___ if it is defined in a ___4___. Use the keyword ___2___ to refer to the ___2___ variable inside a ___4___.'''
hard_quiz = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
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

# save the quiz and answer in a dictionary for easier refering
quiz_and_answer_list = {
'easy': [easy_quiz, ['God', 'details', 'two', 'third']],
'medium': [medium_quiz, ['variable', 'global', 'local', 'function']],
'hard': [hard_quiz, ['function', 'arguments', 'None', 'list']]  
}

# no more than 5 chances, otherwise game over.
number_of_guess = 5

# try to guess each blanks right, otherwise exit the game after number_of_guess tries.
def guess_until_right(index, value, guess, quiz_local):
    # have to tell Python it's the global variables!
    global number_of_guess
    global quiz

    while guess != value:
        number_of_guess -= 1
        if number_of_guess == 1:
            print "That isn't the correct answer! You only have 1 try left!  Make it count!"
        elif number_of_guess == 0:
            print "You've failed too many straight guesses!  Game over!"
            exit(0)
        else:
            print "That isn't the correct answer!  Let's try again; you have %s trys left!" %(number_of_guess)
        print "\n" * 3
        print "The current paragraph reads as such:\n"
        print quiz_local
        guess = raw_input("What should be substituted in for __%s__?" %(index + 1))

    # have a right guess, reset the number_of_guess to 5 again.
    number_of_guess = 5
    quiz = quiz_local.replace("___%s___" %(index + 1), guess)
    print "Correct!\n"
    


# let the user select her levle
level = raw_input("""
Please select a game difficulty by typing it in!
Possible choices include easy, medium, and hard.
""")
print "You've chosen %s!" %(level)
print
print "You will get %s guesses per problem" %(number_of_guess)
print

quiz_and_answer = quiz_and_answer_list[level]
quiz, answer = quiz_and_answer[0], quiz_and_answer[1]

# iterate through the blanks.
for index, value in enumerate(answer):
    if index != len(answer) - 1:
        print "The current paragraph reads as such:"
    print "\n"
    print quiz
    guess = raw_input("What should be substituted in for __%s__?" %(index + 1))
    guess_until_right(index, value, guess, quiz)
    if index == len(answer) - 1:
        print quiz
        print "You won!"




