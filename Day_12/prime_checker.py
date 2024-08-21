def is_prime(num: bool):
    '''
    Check if a number is prime on not
    return true for prime, false otherwise
    '''
    for i in range(1, int(num//2)):
        if num % i != 0:
            check = True
        else:
            check = False
    return check


num = int(input('Please enter an integer: > '))
print(is_prime(num))

# Works her but not on the portal for the course.
