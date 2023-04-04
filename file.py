num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #variable declaration
string = 'Hello World' #log statement
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #Tuples
print(type(fruit)) #type check
print(pizza_toppings[1]) #access value
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #access value
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #add value
print(fruit[2]) #access value

# - conditional
#     - if
#     - else if
#     - else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower") 


# - conditional
#     - if
#     - else if
#     - else
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loop
for x in range(5): #increment
    print(x)
    # - start
    # - stop
for x in range(2,5): 
    print(x)
    # - start
    # - stop
    # - increment
for x in range(2,10,3):
    print(x)
x = 0 #variable declaration
while loop
    # - start
    # - stop
    # - increment
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() #delete value
pizza_toppings.pop(1)#delete value

print(person)
person.pop('eye_color') #delete value
print(person)


for topping in pizza_toppings:#for loop
    if topping == 'Pepperoni': #Conditional
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #- break

def print_hello_ten_times():#parameter
    for num in range(10):#increment
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): #parameter
    for num in range(x):#increment
        print('Hello')

print_hello_x_times(4) #argument

def print_hello_x_or_ten_times(x = 10):#parameter
    for num in range(x):#increment
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4) #argument


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)