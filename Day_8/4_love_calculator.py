def calculate_love_score(name_1, name_2) -> int:

    result: int = 0
    for i in range(0, len(name_1)):
        if name_1[i].lower() == 't':
            result += 1
        elif name_1[i].lower() == 'r':
            result += 1
        elif name_1[i].lower() == 'u':
            result += 1
        elif name_1[i].lower() == 'e':
            result += 1

    for i in range(0, len(name_2)):
        if name_2[i].lower() == 't':
            result = result + 1
        elif name_2[i].lower() == 'r':
            result = result + 1
        elif name_2[i].lower() == 'u':
            result = result + 1
        elif name_2[i].lower() == 'e':
            result = result + 1

    return result


n_1 = input('What is your name? > ')
n_2 = input('What is your crushes name? > ')
score = calculate_love_score(n_1, n_2)
print(score)

# Works fine here, gets stuck on line 27 in the online editor used in the course.  Think it might be the input statement
# causing EOF to throw there.
