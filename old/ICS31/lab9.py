# Khuong Tiet 88812261 and Linh Chu 10473576  Lab sec 10. Lab Asst. 9

print()
print('**************************')
print('-------- Part (C) --------')
print('**************************')

NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4  # 3 choices is A/B/C, 4 choices is A/B/C/D, 5 is A/B/C/D/E

print()
print('---- c.1 ----')
print()

from collections import namedtuple
from random import randrange
from random import choice

def generate_answers() -> str:
    ''' Generates and returns a string of letters representing possible answers
        on a test
    '''
    answers =""
    choices = 'ABCDE'
    for i in range(NUMBER_OF_QUESTIONS):
        answers += choice(choices[:NUMBER_OF_CHOICES])
    return answers

ANSWERS = generate_answers()

#c.2
"""
Student = namedtuple('Student', 'ID answers')
s1 = Student('12345678', 'ABCCDAABAABCBBCACCAD')
s2 = Student('87654321',  'BADACCABADCCABDDCBAB')

def random_students() -> [Student]:
    result = []
    for i in range(NUMBER_OF_STUDENTS):
        ID_NUM = ''
        for i in range(8):
            ID_NUM += str(randrange(9))
        result.append(Student(ID_NUM, generate_answers()))
    return result
"""
#c.3
Student = namedtuple('Student', 'ID answers scores total')
s1 = Student('12345678', 'ABCCDAABAABCBBCACCAD', [1, 0, 1, 1, 1, 0, ...], 10)
s2 = Student('87654321',  'BADACCABADCCABDDCBAB', [0, 1, 0, 0, 0, 1, ...], 5)

def random_students() -> [Student]:
    result = []
    for i in range(NUMBER_OF_STUDENTS):
        ID_NUM = ''
        for i in range(8):
            ID_NUM += str(randrange(9))

        STUDENT_ANSWER = generate_answers()
        count = 0
        CORRECT_ANSWER = []
        for i in range(len(ANSWERS)):
            if ANSWERS[i] == STUDENT_ANSWER[count]:
                CORRECT_ANSWER.append(1)
            else:
                CORRECT_ANSWER.append(0)
            count += 1
            
        TOTAL_SCORE = sum(CORRECT_ANSWER)
        result.append(Student(ID_NUM, STUDENT_ANSWER,CORRECT_ANSWER,TOTAL_SCORE))
    return result

def top_score_from_students(s: Student) -> int:
    return s.total
        
def top_scores(j: list):
    j.sort(key = top_score_from_students, reverse = True)
    print(j[:10])
    score_list = []
    for i in j:
        score_list.append(i.total)
    print("Mean = " + str(sum(score_list)/len(score_list)))

print(top_scores(random_students()))

#c.4

def generate_weighted_student_answer(correct_answer: str) -> str:
    answer = 'ABCD'
    answer += correct_answer
    return choice(answer)

def random_students2() -> [Student]:
    result = []
    for i in range(NUMBER_OF_STUDENTS):
        ID_NUM = ''
        for i in range(8):
            ID_NUM += str(randrange(9))
        STUDENT_ANSWER = ''
        CORRECT_ANSWER = []
        for i in ANSWERS:
            local_answer = generate_weighted_student_answer(i)
            STUDENT_ANSWER += local_answer
            if i == local_answer:
                CORRECT_ANSWER.append(1)
            else:
                CORRECT_ANSWER.append(0)
        TOTAL_SCORE = sum(CORRECT_ANSWER)
        result.append(Student(ID_NUM, STUDENT_ANSWER,CORRECT_ANSWER,TOTAL_SCORE))
    return result
print(top_scores(random_students2()))

def question_weights(S : [Student]) -> list:
    result = [0] * 20
    for i in S:
        for j in range(len(i.scores)):
            if i.scores[j] == 0:
                result[j] = result[j] + 1
    return result

WEIGHT_SCORE = question_weights(random_students2())


#d.1

def calculate_GPA(GPA: 'list of letter grades') -> float:
    calculate = 0
    for i in GPA:
        if i == 'A':
            calculate = calculate + 4
        elif i == 'B':
            calculate = calculate + 3
        elif i == 'C':
            calculate = calculate + 2
        elif i == 'D':
            calculate = calculate + 1
        else:
            calculate = calculate + 0
    final_GPA = calculate / len(GPA)
    return final_GPA

def calculate_GPA2(GPA: 'list of letter grades') -> float:
    calculate = 0
    grade = {
        "A" : 4,
        "B" : 3,
        "C" : 2,
        "D" : 1,
        "F" : 0}
    for i in GPA:
        calculate += grade[i]
        
    return calculate/len(GPA)

def flatten_2D_list(x: [list]) -> list:
    result = []
    for i in x:
        for o in i:
            result.append(o)
    return result

def skip_every_third_item(x: list) -> list:
    result = []
    for i in x:
        if (x.index(i) + 1) % 3 != 0:
            result.append(i)
    return result

def skip_every_nth_item(x: list, n: int) -> list:
    result = []
    for i in x:
        if (x.index(i) + 1) % n != 0:
            result.append(i)
    return result
def tally_days_worked(x: list) -> dict:
    result = {}
    for i in x:
        if not i in result:
            result[i] = 1
        else:
            result[i] += 1
    return result






























