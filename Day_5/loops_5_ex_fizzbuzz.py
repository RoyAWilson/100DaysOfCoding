'''
Replicate the fizzbuzz game using for loops.

Rules:

1. Your program should print each number from 1 to 100 in turn and include number 100.

2. But when the number is divisible by 3 then instead of printing the number it should print "Fizz".

3. When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

4. And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

'''

for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print('Fizzbuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
# Did this one in Giles' course too.
