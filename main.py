#Find if two numbers are amicable

def find_proper_factors(number):
    proper_factors = []

    for factor in range (1,number): #for every integer between 1 and the number
        if number % factor == 0:
            proper_factors.append(factor)

    return proper_factors

def sum_proper_factors(proper_factors):
    sum_of_factors = 0

    for num in proper_factors:
        sum_of_factors += num

    return sum_of_factors

def get_number():
    number = -1

    not_valid = True
    while not_valid:
        try:
            number = int(input("Please enter a number: "))
        except ValueError:
            print ("Please enter an integer.")

        if number > 0:
            not_valid = False
        else:
            print ("Please enter an integer bigger than 0.")

    return number

number1 = get_number()
number2 = get_number()

number1_factors = find_proper_factors(number1)
number2_factors = find_proper_factors(number2)

if sum_proper_factors(number1_factors) == number2 and sum_proper_factors(number2_factors) ==  number1:
    print ("amicable")
else:
    print ("not amicable")