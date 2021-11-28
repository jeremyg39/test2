number = int(input("Enter a number: "))
while number % 3 == 0:
    print("fizz")
    break
while number % 5 == 0:
    print("buzz")
    break
while number % 5 == 0 and number % 3 == 0:
    print("fizzbuzz")
    break
if number % 3 != 0 and number % 5 != 0:
    print("Choose a better number")
