# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 

hot_dog = (float(3.50))

chili_dog = (float(4.50))

cheese = (float(0.50))

peppers = (float(0.75))

grilled_onions = (float(1.00))

print ('Do you want a hot dog or a chili dog?')
hot_dog_type = (input('enter hot dog or chili dog: '))
if hot_dog_type == 'hot dog':
    hot_dog_type = hot_dog
elif hot_dog_type == 'chili dog':
    hot_dog_type = chili_dog

add_cheese = (input('Do you want cheese? enter yes or no: '))
if add_cheese == 'yes':
    add_cheese = cheese
elif add_cheese == 'no':
    add_cheese = 0

add_peppers = (input('Do you want a pepper? enter yes or no: '))
if add_peppers == 'yes':
    add_peppers = peppers
elif add_peppers == 'no':
    add_peppers = 0

add_grilled_onions = (input('Do you want grilled onions? enter yes or no: '))
if add_grilled_onions == 'yes':
    add_grilled_onions = grilled_onions
elif add_grilled_onions == 'no':
    add_grilled_onions = 0

sub_total = hot_dog_type + add_cheese + add_peppers + add_grilled_onions
tax = sub_total * 0.07
total = sub_total + tax

print (f'sub total is ${sub_total:.2f}')
print (f'tax is: ${tax:.2f}')
print (f'total is: ${total:.2f}')