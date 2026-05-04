from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\nAnswer: ",
    "What color are bananas?\n(a) Red\n(b) Blue\n(c) Yellow\nAnswer: ",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Purple\nAnswer: ",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You got {score}/{len(questions)} right.")        


run_test(questions)