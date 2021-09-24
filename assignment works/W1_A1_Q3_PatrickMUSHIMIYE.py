# A program to make ALU Hangman
# this initial steps inviting player for a game
print("welcome to hangman game")
name = input("please input your name\n")
print("Hello" + " " + name + " " + "Good luck")
print("10 question about ALU")
# this is the list of both questions and answers
question = ["When was ALU founded?", "Who is the CEO of ALU?", "Where are ALU campuses?",
            "How many campuses does ALU have?", "What is the name of ALU Rwanda’s Dean?",
            "Who is in charge of Student Life?", "What is the name of our Lab?",
            "How many students do we have in Year 2 CS?", "How many degrees does ALU offer?",
            "Where are the headquarters of ALU?", ]
answers = ['2015', "Fred Swaniker", "Rwanda and Mauritius", '2', "Insert deans name", "Sila Ogidi",
           "Insert name here", "Put the numbers of student", '8', "Mauritius", ]
RA = 0  # this is the variable that store the right answers
# the loop to iterate list of question and their answer till execution exhausted
for count in range(9):
    answer = input(question[count])
    if answer == answers[count]:  # condition for checking whether the answer is in list of answers or not
        RA += 1  # increment the variable name right answer by 1
    else:
        print("you are hanging the man")
    if RA == 0 and count == 5:
        break  # break keyword will stop the loop when the user wrong the question 6 times
if RA >= 6:  # condition that depict whether man should live or not
    print("the man lives")
else:
    print("the man lost their lives")
