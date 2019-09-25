from Question import Question
import sys as sistem

question_prompts = [
    "1. ¿What color are apples?\n(a) Red/Green\n(b) Purble\n(c) Orange\n\n",
    "\n2. ¿What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "\n3. ¿What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

print("\n ********* Questions Loaded!... ********* \n")
name_player = str(str.capitalize(input("Write your name: ")))
resp = str(input("Hello "+ name_player +" are you ready play game? write yes or no for continue: "))
print("\n")
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("\n")
    print(name_player +" you got " + str(score) + "/" + str(len(questions)) + " correct")

if resp == "YES" or resp == "Yes" or resp == "yes" or resp == "Y" or resp == "y":
    run_test(questions)
    print("\n")
    print("********** FINISHED QUESTIONS **********")
else:
    print("See you son!...")
    sistem.exit()