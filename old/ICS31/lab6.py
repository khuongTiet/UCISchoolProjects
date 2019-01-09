# Khuong Tiet 88812261 and Jacqueline Lee 25723713. ICS 31 Lab sec 10. Lab asst 6.

print()
print('-------- Part (C) --------')
print()
print('---- c.1 ----')
print()

def contains(string1: str, string2: str) -> bool:
    ''' Takes two strings and returns True/False if the second one occurs in the first one '''
    return string2 in string1

assert contains('banana', 'ana')
assert not contains('racecar', 'ck')
assert contains('Alphabet', 'bet')
assert not contains('Anteater', 'cow')

print()
print('---- c.2 ----')
print()

def sentence_stats(string:str):
    ''' Takes a string and returns statistics on the string '''
    c = len(string)
    l = string.split(' ')
    words = len(l)
    num = 0
    for i in l:
        num += len(i)
    aveLen = num/words
    print("Characters:", c)
    print("Words:", words)
    print("Average word length:", aveLen)
print(sentence_stats("I love UCI"))

print()
print('---- c.3 ----')
print()

def initials(full_name: str)-> str:
    ''' Takes a name and returns the initials capitalized '''
    name = full_name.split(' ')
    full = ''
    for i in name:
        full += i[0].upper()
    return full
assert initials('Bill Cosby') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'

print()
print('-------- Part (D) --------')
print()
print('---- d.1 ----')
print()

from random import randrange

for i in range(50):
    print(randrange(11))
print()
print()
for j in range(50):
    print(randrange(1,7))
    
print()
print('---- d.2 ----')
print()

def roll2dice() -> int:
    ''' Returns a number that reflects a random roll of two dice '''
    roll1 = randrange(1,7)
    roll2 = randrange(1,7)
    return roll1 + roll2
for i in range(50):
	print(roll2dice())

print()
print('---- d.3 ----')
print()

def distribution_of_rolls(num: int):
    '''Prints the distribution of the values of num rolls'''
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    num7 = 0
    num8 = 0
    num9 = 0
    num10 = 0
    num11 = 0
    num12 = 0
    for i in range(num):
        x = roll2dice()
        if x == 2:
            num2 += 1
        elif x == 3:
            num3 +=1
        elif x == 4:
            num4 += 1
        elif x == 5:
            num5 += 1
        elif x == 6:
            num6 += 1
        elif x == 7:
            num7 += 1
        elif x == 8:
            num8 += 1
        elif x == 9:
            num9 += 1
        elif x == 10:
            num10 += 1
        elif x == 11:
            num11 += 1
        else:
            num12 += 1
    print('2:    {} ( {} %)    {}'.format(num2, num2/num*100, num2*'*'))
    print('3:    {} ( {} %)    {}'.format(num3, num3/num*100, num3*'*'))
    print('4:    {} ( {} %)    {}'.format(num4, num4/num*100, num4*'*'))
    print('5:    {} ( {} %)    {}'.format(num5, num5/num*100, num5*'*'))
    print('6:    {} ( {} %)    {}'.format(num6, num6/num*100, num6*'*'))
    print('7:    {} ( {} %)    {}'.format(num7, num7/num*100, num7*'*'))
    print('8:    {} ( {} %)    {}'.format(num8, num8/num*100, num8*'*'))
    print('9:    {} ( {} %)    {}'.format(num9, num9/num*100, num9*'*'))
    print('10:   {} ( {} %)    {}'.format(num10, num10/num*100, num10*'*'))
    print('11:   {} ( {} %)    {}'.format(num11, num11/num*100, num11*'*'))
    print('12:   {} ( {} %)    {}'.format(num12, num12/num*100, num12*'*'))
    print('-----------------------------')
    print('    ', num, "rolls")
distribution_of_rolls(200)

print()
print('-------- Part (E) --------')
print()
print('---- e.4 ----')
print()

def Caesar_encrypt(transstr: str, howfar: int) -> str:
    ''' Takes a string and returns an encrypted one based on the integer '''
    table = str.maketrans('abcdefghijklmnopqrstuvwxyz', rotate_alphabet(howfar))
    return transstr.translate(table)

def Caesar_decrypt(transstr:str, howfar:int)->str:
    '''Takes a string and returns a decrypted string based on the integer'''
    table = str.maketrans('abcdefghijklmnopqrstuvwxyz', rotate_alphabet(howfar*-1))
    return transstr.translate(table)
        
def rotate_alphabet(order: int) -> str:
    ''' Takes a number and rotates the alphabet based on the number '''
    Alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newAlpha = Alphabet[order:] + Alphabet[:order]
    return newAlpha

print(Caesar_encrypt('Hi there', 3))
print(Caesar_encrypt('kl wkhuh', 3))

print()
print('---- e.2 ----')
print()


print()
print('---- e.3 ----')
print()


print()
print('-------- Part (F) --------')
print()
print('---- f.1 ----')
print()

def print_line_numbers(printline: list):
    ''' Takes a list of strings and prints each string preceded by a line number '''
    for i in range(len(printline)):
        print('{}: {}'.format(i+1, printline[i]))

print()
print('---- f.2 ----')
print()

def stats(listofstring: list):
    lenstr = len(listofstring)
    numEmpty = 0
    nonEmptyList = []
    for j in listofstring:
        if j.isspace() == True:
            numEmpty += 1
        else:
            nonEmptyList.append(j)
    aveChar = 0
    for i in listofstring:
        aveChar += len(i)
    aveChar = aveChar/len(listofstring)
    aveCharNonEmpty = 0
    for x in nonEmptyList:
        aveCharNonEmpty += len(x)
    aveCharNonEmpty = aveCharNonEmpty/len(nonEmptyList)

    print('{}    lines in the list \n{}    empty lines\n{}    average characters per line\n{} average characters per non-empty line'.format(lenstr, numEmpty, aveChar, aveCharNonEmpty))

print()
print('---- f.3 ----')
print()

def list_of_words(listofstring: list)-> list:
    ''' Takes a list of strings and returns a list of individual words with all white space and punctuation removed '''
    wordlist = []
    for i in listofstring:
        k = i.split(' ')
        for j in k:
            remove(' ')
    return wordlist
            




    
