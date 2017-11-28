_author_ = 'Karlie Sanders'


# Calculate golf score when 9 holes have a par of 3 per hole, or 27 total.
# It will then compare your score to some course records
#
#
def welcome():
    print("Enter your score on 9 holes in golf and get you your score and see if you made a course record.")


def valid_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def get_int(prompt):
    value = 0

    value = input(prompt)
    while not valid_int(value):
        print("enter a number between 1 and 15")
        value = input(prompt)
    return int(value)


def get_score():
    print("Please enter your score for hole 1 through 9.")
    score = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    index = 0
    while index < len(score):
        score[index] = get_int('Enter the score for hole ' + str(index + 1) + ': ')
        index += 1
    return score


def get_analysis(score):
    print("Your total score for the round is: ", sum(score))
    print("The lowest score for the round is:", min(score))
    print("The highest score for the round is:", max(score))
    print("The average score for the round is: ", sum(score)/len(score))


def course_records():
    course_record = [20, 21, 20, 19]
    print("The course records for the past four years are: ", course_record)


def main():
    welcome()
    score = get_score()
    get_analysis(score)
    course_records()

main()
