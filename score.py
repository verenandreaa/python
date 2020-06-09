def read_test_scores():
    scores = []
    num_tests = 7
    print("ENTER ALL TEST SCORES: ")
    for i in range(num_tests):
        score = input("Test " + str(i + 1) + ":")
        scores.append(int(score))    

    return sum(scores) / num_tests    


def compute_final_score(average, exam_score):
    score = 0.4 * average + 0.6 * exam_score
    return score    


def get_letter_grade(finalized_score):
    if 90 <= finalized_score <= 100:
        letter_grade = 'A'
    elif 80 <= finalized_score <= 89:
        letter_grade = 'B'
    elif 70 <= finalized_score <= 79:
        letter_grade = 'C'
    elif 60 <= finalized_score <= 69:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    return letter_grade    


def print_comment(letter_grade):    
    if letter_grade == 'A':
        print("COMMENT:            Very Good")
    elif letter_grade == 'B':
        print("COMMENT:            Good")
    elif letter_grade == 'C':
        print("COMMENT:            Satisfactory")
    elif letter_grade == 'D':
        print("COMMENT:            Need Improvement")
    elif letter_grade == 'F':
        print("COMMENT:            Poor")    


def get_student_id():
    print("ENTER STUDENT ID: ")
    identity = int(input())
    return identity    


def get_exam_score():
    print("ENTER EXAM SCORE: ")
    exam_score = int(input())
    return exam_score    


if __name__ == '__main__':
    student_id = get_student_id()
    exam = get_exam_score()
    tavge = read_test_scores()
    print("TEST AVERAGE IS:    " + str(tavge))
    final_score = compute_final_score(tavge, exam)
    print("FINAL SCORE IS:     " + str(final_score))
    grade = get_letter_grade(final_score)
    print("LETTER GRADE IS:     " + str(grade))
    print_comment(grade)