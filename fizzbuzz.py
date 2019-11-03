# FizzBuzz変換 100まで
def fizzbuzz_convert(number):
    if number % 15 == 0:
        return 'FizzBuzz'
    if number % 5 == 0:
        return 'Buzz'
    if number % 3 == 0:
        return 'Fizz'
    return number


for number in range(1, 101):
    print(fizzbuzz_convert(number))
