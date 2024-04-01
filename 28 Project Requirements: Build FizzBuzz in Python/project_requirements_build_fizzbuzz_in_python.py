#Multiples of 3 print "Fizz" instead of the number
#Multiples of 5 print "Buzz". 
#For numbers which are multiples of both 3 and 5 print "FizzBuzz".


def fizz_buzz(max_value):
    for num in range(1, max_value + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

 
fizz_buzz(100)