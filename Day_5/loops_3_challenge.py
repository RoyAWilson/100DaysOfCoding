'''
Challenge to replicate the max function on a list of nubmers
'''

scores: list = [180, 124, 165, 173, 189, 169, 146]

high: int = 0

# Build a loop to have high always equal to the highest number so far encountered

for score in scores:
    if score > high:
        high = score
print(f'The maximum score is:  {high}')
