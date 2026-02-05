# Write a program that asks the user to enter a person's age.  The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult.  Following are the guidelines:

# If the person is 1 year old or less, it should display "infant" (without quotes).
# If the person is older than 1 year, but younger than 13 years, it should display "child".
# If the person is at least 13 years old, but less than 20 years old, it should display "teenager".
# If the person is at least 20 year old, it should display "adult".


    ######################
    # WRITE YOUR CODE HERE
    ######################

age = float(input("Enter the person's age: "))
if age > 0 and age <= 1:
    print("infant")
elif age > 1 and age < 13:
    print("child")
elif age >= 13 and age < 20:
    print("teenager")
elif age >= 20:
    print ("adult")

   


#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
