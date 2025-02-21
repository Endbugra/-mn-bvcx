def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return print("FizzBuzz")
    elif number % 3 == 0:
        return print("Fizz")
    elif number % 5 == 0:
        return print("Buzz")
    else:
        return str(number)