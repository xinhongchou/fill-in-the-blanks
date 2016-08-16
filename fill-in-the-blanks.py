# IPND Stage 2 Final Project

# quizs
easy_quiz = '''___1___ hides in the ___2___.
There are ___3___ ways to write error-free programs; only the ___4___ one works.'''
medium_quiz = '''A ___1___ is defined by default as a ___2___ ___1___ if defined outside of functions.
A ___1___ is ___3___ if it is defined in a ___4___. Use the keyword ___2___ to refer to the ___2___ variable inside a ___4___.'''
hard_quiz = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''


# save the quiz and answer in a dictionary for easier refering
quiz_and_answer_list = {
'easy': [easy_quiz, ['God', 'details', 'two', 'third']],
'medium': [medium_quiz, ['variable', 'global', 'local', 'function']],
'hard': [hard_quiz, ['function', 'arguments', 'None', 'list']]  
}

# no more than 5 chances, otherwise game over.
number_of_guess = 5

def guess_until_right(index, value, guess, quiz):
    """Try to guess each blanks right, otherwise exit the game after number_of_guess tries.

    Args:
        index: the (index + 1)th blank.
        value: the correct answer of the blank.
        guess: the initial guess
        quiz: the whole quiz sentence.

    Return:
        the new quiz with the (index + 1)th blank filled.
    """
    # have to tell Python it's the global variables,
    # otherwise it will be a local variable again.
    global number_of_guess

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
        print quiz
        guess = raw_input("What should be substituted in for __%s__?" %(index + 1))

    # have a right guess, reset the number_of_guess to 5 again.
    number_of_guess = 5
    return quiz.replace("___%s___" %(index + 1), guess)
    


def play_game():
    """ The entry point to play the game.
    """
    # let the user select her levle
    level = raw_input("""
    Please select a game difficulty by typing it in!
    Possible choices include easy, medium, and hard.
    """)
    print "You've chosen %s!\n" %(level)
    print "You will get %s guesses per problem\n" %(number_of_guess)

    quiz_and_answer = quiz_and_answer_list[level]
    quiz, answer = quiz_and_answer[0], quiz_and_answer[1]

    # iterate through the blanks.
    for index, value in enumerate(answer):
        if index != len(answer) - 1:
            print "The current paragraph reads as such:\n"
        print quiz
        guess = raw_input("What should be substituted in for __%s__?" %(index + 1))
        quiz = guess_until_right(index, value, guess, quiz)
        if index == len(answer) - 1:
            print quiz
            print "You won!"
        else:
            print "Correct!\n"

# let's the fun begin!
play_game()




