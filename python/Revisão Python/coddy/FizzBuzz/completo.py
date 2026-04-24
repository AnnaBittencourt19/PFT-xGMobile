print("Welcome to FizzBuzz!")

def fizzbuzz(num):
    tem_3 = "3" in str(num)

    if (num % 3 == 0) and (num % 7 == 0):
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 7 == 0:
        return "Buzz"
    elif (not(num % 3 == 0)) and tem_3:
        return "Almost Fizz"
    else:
        return num


entrada = int(input())

for i in range(1, entrada+1):
    resultado = fizzbuzz(i)
    print(resultado)