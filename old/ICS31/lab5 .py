# Khuong Tiet 88812261 and Brian Mangubat 18766571 Lab sec. 10, Lab asst. 5

print()
print('-------- part (C) --------')
print()
print('---- c.1 ----')
print()

from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')
D1 = Dish('California Roll', 10.00, 500)
D2 = Dish('McDouble', 1.50, 600)
D3 = Dish('Orange Chicken', 7.00, 600)

print()
print('---- c.2 ----')
print()

def Dish_str(x: namedtuple) -> str:
    ''' Returns a string in organized form '''
    string = x.name+' ($'+str(x.price)+')'+' : '+str(x.calories)+ ' cal'
    return string
	
print()
print('---- c.3 ----')
print()

def Dish_same(dish1: Dish, dish2: Dish) -> bool:
    ''' Takes two dishes and returns True/False if calories match '''
    return dish1.calories == dish2.calories
assert not Dish_same(D1, D2)
assert Dish_same(D2, D3)

print()
print('---- c.4 ----')
print()

def Dish_change_price(x: 'Dish', y: int) -> Dish:
    '''Takes a dish and makes a new dish with changed price'''
    x = x._replace(price = x.price + y*.01 * x.price)
    return x

print()
print('---- c.5 ----')
print()

def Dish_is_cheap(x: Dish, y:int) -> bool:
    '''Takes a dish and returns True/False if the number is greater/lower than the number inputted'''
    return x.price < y
assert Dish_is_cheap(D1, 11)
assert not Dish_is_cheap(D3, 5)

print()
print('---- c.6 ----')
print()

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

print()
print('---- c.7 ----')
print()

def Dishlist_all_cheap(x: 'list of Dishes', number: int) -> bool:
    '''returns true or false if every dish is cheaper than the number inputted'''
    for i in x:
       return Dish_is_cheap(i,number)

assert Dishlist_all_cheap(DL, 11)
assert not Dishlist_all_cheap(DL, 9)

print()
print('---- c.8 ----')
print()

def Dishlist_change_price(dishlist: 'list of Dishes', percent: int) -> 'list of Dishes':
    ''' Takes a list of dishes and raises its price by the specified percent '''
    changedprice = []
    for i in dishlist:
        k = Dish_change_price(i, percent)
        changedprice.append(k)
    return changedprice

print()
print('---- c.9 ----')
print()

def Dishlist_prices(dishlist: 'list of numbers') -> list:
    '''returns list of numbers of the prices of the dishes on the list'''
    dishprices = []
    for i in dishlist:
        dishprices.append(i.price)
    return dishprices

print()
print('---- c.10 ----')
print()

def Dishlist_average(dishlist: list) -> float:
    '''Takes a list of dishes and returns the average price of dishes'''
    k = sum(Dishlist_prices(dishlist))/len(dishlist)
    return k

print()
print('---- c.11 ----')
print()

def Dishlist_keep_cheap(dishlist: 'list of Dishes', price: float) -> 'list of Dishes':
    ''' Takes a list of Dishes and a number and returns dishes that are cheaper than the inputted number '''
    keepcheap = []
    for i in dishlist:
        if Dish_is_cheap(i, price) == True:
            keepcheap.append(i)
    return keepcheap

print()
print('---- c.12 ----')
print()

DL12 = [
    Dish("Carne Asada Burrito", 10.50, 900),
    Dish("Chicken Nuggets", 5.00, 700),
    Dish("Hamburger", 1.00, 300),
    Dish("Caesar Salad", 8.00, 200),
    Dish("French Fries", 2.00, 400),
    Dish("Alphabet Soup", 3.00, 500),
    Dish("Orange Chicken", 6.00, 600),
    Dish("Cajun Fries", 4.00, 500),
    Dish("Teriyaki Chicken", 7.00, 600),
    Dish("Caramel Apple", 5.00, 700),
    Dish("French Onion Soup", 8.00, 900),
    Dish("Steak and Shrimp", 21.00, 1200),
    Dish("Lobster", 20.00, 1000),
    Dish("Carbonara", 12.00, 900),
    Dish("Chicken Alfredo", 13.00, 700),
    Dish("Sushi Burrito", 11.00, 800),
    Dish("Curry", 10.00, 700),
    Dish("Pho", 9.00, 800),
    Dish("Puto", 8.00, 500),
    Dish("Escargot", 17.00, 900),
    Dish("Caviar", 30.00, 200),
    Dish("Mashed Potatoes", 6.00, 800),
    Dish("Tacos", 2.00, 400),
    Dish("Carne Asada Fries", 7.25, 900),
    Dish("Pulled Pork Sandwich", 8.00, 850)]

def before_and_after():
    ''' prompts user for a percentage in change of prices then prints out the changes'''
    change = input('Enter a percentage in change of prices: ')
    print(Dishlist_display(DL12))
    k = Dishlist_change_price(DL12, int(change))
    print(Dishlist_display(k))

print()
print('-------- part (D) --------')
print()
print('---- d.1 ----')
print()

print()
print('---- d.2 ----')
print()

print()
print('---- d.3 ----')
print()

print()
print('-------- part (E) --------')
print()

Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])

print()
print('---- e.1 ----')
print()

r3 = Restaurant('Pascal', 'French', '940-752-0107', [Dish('Escargots', 12.95, 250),
                                                     Dish('Poached Salmon', 18.50, 550),
                                                     Dish('Rack of Lamb', 24.00, 850),
                                                     Dish('Marjolaine Cake', 8.50, 950)])

print()
print('---- e.2 ----')
print()

def Restaurant_first_dish_name(R: 'Restaurant') -> str:
    '''Returns the name of the first dish on the restaurant's menu'''
    return R.menu[0][0]
assert Restaurant_first_dish_name(r1) == 'Mee Krob'
assert Restaurant_first_dish_name(r2) == 'Homard Bleu'

print()
print('---- e.3 ----')
print()

def Restaurant_is_cheap(R: 'Restaurant', number: 'price') -> bool:
    ''' Takes a restaurant and a price and checks if that returns True/False '''
    k = sum(Dishlist_prices(R.menu))/len(R.menu)
    return k < number

print()
print('---- e.4 ----')
print()
