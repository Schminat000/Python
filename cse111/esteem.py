
def list_questions():
    print("""
    1. I feel that I am a person of worth, at least on an equal plane with others. \n
    2. I feel that I have a number of good qualities. \n
    3. All in all, I am inclined to feel that I am a failure. \n
    4. I am able to do things as well as most other people. \n
    5. I feel I do not have much to be proud of. \n
    6. I take a positive attitude toward myself. \n
    7. On the whole, I am satisfied with myself. \n
    8. I wish I could have more respect for myself. \n
    9. I certainly feel useless at times. \n
    10. At times I think I am no good at all. \n""")


def ask_questions():
    responses = []

    print("""
        Strongly Disagree (D)
        Disagree (d)
        Agree (a)
        Strongly Agree (A) \n
        """)

    for i in range(0, 10):
        responses.append(
            input(f"What is your response for statement {i + 1}?"))

    return responses


def calc_response(responses):
    score = 0
    for i in range(0, 10):
        if i + 1 == 1 or i + 1 == 2 or i + 1 == 4 or i + 1 == 6 or i + 1 == 7:
            if responses[i] == "D":
                pass
            elif responses[i] == "d":
                score += 1
            elif responses[i] == "a":
                score += 2
            else:
                score += 3
        elif i + 1 == 3 or i + 1 == 5 or i + 1 == 8 or i + 1 == 9 or i + 1 == 10:
            if responses[i] == "D":
                score += 3
            elif responses[i] == "d":
                score += 2
            elif responses[i] == "a":
                score += 1
            else:
                pass
        else:
            print("Error")

    return score


def main():
    list_questions()
    responses = []
    responses = ask_questions()
    score = calc_response(responses)

    print(f"Your score is {score}")
    print("A Score below 15 may indicate problematic low self-esteem")


main()
