# Tiet 88812261 and Mitchell Chan 63266718.  ICS Lab 31 4, Session 10

print('---------- Part (c) ----------')

def test_number (n: int, m: str)-> bool:
    ''' Returns True if the number has property of string '''
    m == 'even' or 'odd' or 'positive' or 'negative'
    
    if m == 'positive':
        if n >= 0:
            return True
        else:
            return False
    elif m == 'negative':
        if n <= 0:
            return True
        else:
            return False
    elif m == 'even':
        if n%2 == 0:
            return True
        else:
            return False
    elif m == 'odd':
        if n%2 != 0:
            return True
        else:
            return False
   
assert test_number(14, 'even')
assert not test_number(100, 'odd')
assert test_number(33, 'positive')
assert not test_number(100, 'negative')
print('')

def display():
    ''' Return the string printed one letter per line'''
    x = input('Enter a word:')
    for i in x:
        print(i)
print(display())
print('')

def square_list(n: list) -> int:
    ''' Returns a list of integers squared '''
    for i in n:
        print (i**2)
print('')

def match_first_letter(s: str,  l: list) -> str:
    ''' Returns the strings in the list that start with the 1-character string'''
    for i in l:
        for n in i:
            if s == n[0]:
                print(i)
match_first_letter('I', ['Iron Man', 'Iron Man 2', 'The Avengers', 'Superman', 'I am Legend'])
print('')

def match_area_code(area_code: list, phone_numbers: list) -> str:
    ''' Returns the numbers with the matching area code '''
    for i in phone_numbers:
        for d in area_code:
            if d == i[1:4]:
                print(i)
match_area_code(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234'])

print('')

def matching_area_codes(area_code: list, phone_numbers: list) -> list:
    ''' Returns the numbers with the matching area code '''
    a = []
    for i in phone_numbers:
        for d in area_code:
            if d == i[1:4]:
                a.append(i)
                print(a)
matching_area_codes(['949', '714'], ['(714)824-1234', '(419)312-8732', '(949)555-1234'])
print('')

def is_vowel(onechar: str) -> bool:
    ''' Returns True or False if input string is a vowel '''
    if onechar in 'aeiouAEIOU':
        
         

