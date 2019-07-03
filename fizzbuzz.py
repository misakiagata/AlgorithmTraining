#FizzBuzz
def fizzbuzz(number):
    if number%3==0 and number%5==0:
        print('FizzBuzz')
    elif number%3==0:
        print('Fizz')
    elif number%5==0:
        print('Buzz')
    else:
        pass

userInputNumber = input('Input number: ')
fizzbuzz(int(userInputNumber))