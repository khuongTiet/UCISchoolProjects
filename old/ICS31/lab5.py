# Khuong Tiet 88812261 and Brian Mangubat 18766571

print()
print('-------- part (C) --------')
print()
print('---- c.1 ----')
from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')
D1 = Dish('California Roll', 10.00, 500)
D2 = Dish('McDouble', 1.50, 600)
D3 = Dish('Orange Chicken', 7.00, 600)

print('---- c.2 ----')
def Dish_str(x: namedtuple) -> str:
    ''' Returns a string in organized form '''
    string = x.name+' ($'+str(x.price)+')'+' : '+str(x.calories)+ ' cal'
    return string
print('---- c.3 ----')
def Dish_same(dish1: Dish, dish2: Dish) -> bool:
    ''' Takes two dishes and returns True/False if calories match '''
    return dish1.calories == dish2.calories
assert not Dish_same(D1, D2)
assert Dish_same(D2, D3)

print('---- c.4 ----')
def Dish_change_price(x: 'Dish', y: int) -> Dish:
    '''Takes a dish and makes a new dish with changed price'''
    x = x._replace(price = x.price + y*.01 * x.price)
    return x

print('---- c.5 ----')
def Dish_is_cheap(x: Dish, y:int) -> bool:
    '''Takes a dish and returns True/False if the number is greater/lower than the number inputted'''
    return y < x.price
assert not Dish_is_cheap(D2, 9)
assert Dish_is_cheap(D1, 9)

print('---- c.6 ----')
DL = [
    Dish("Carne Asada Burrito", 10.50, 900),
    Dish("Chicken Nuggets", 5.00, 700),
    Dish("Hamburger", 1.00, 300),
    Dish("Caesar Salad", 8.00, 200),
    Dish("French Fries", 2.00, 400)]
DL2 = [
    Dish("Ramen", 10.25, 700),
    Dish("Takoyaki", 8.75, 800),
    Dish("Tacos", 1.75, 300),
    Dish("Ice cream", 1.00, 100)]

DL.extend(DL2)

def Dishlist_display(D: 'list of Dishes') -> str:
    ''' Takes a list of dishes and returns a string representation of each dish '''
    display = ''
    for i in D:
        display += (
            "Name:    " +i.name+ "\n" +
            "Price:    $" + str(i.price) + "\n"
            "Calories:    " + str(i.calories) + "\n\n")
    return display

print(Dishlist_display(DL))

print('---- c.7 ----')
def Dishlist_all_cheap(x:'Dishes', y:int) -> bool:
    '''returns true or false if every dish is cheaper than the number inputted'''
    for i in x:
       if Dish_is_cheap(i,y):
           return True
       else:
           return False
        

            
