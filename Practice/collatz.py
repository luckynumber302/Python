import sys

def collatz(number):
    result = None
    
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    
    print(str(result))
    return result
        
print('Please enter a number.')
try:
    keyin = int(input())
except ValueError:
    print('You need to enter an integer.')
    sys.exit()

collatzResult = collatz(keyin)
while collatzResult != 1:
    collatzResult = collatz(collatzResult)