'''
Find the highest student score:
'''
scores = [180, 124, 165, 173, 189, 169, 146]

print(f'Total score = {sum(scores)}')
print(f'Max score = {max(scores)}')
print(f'Min score = {min(scores)}')
print(f'Mean score = {round(sum(scores)/len(scores), 2)}')

# long hand way to get a total score:

tot_score: int = 0

for score in scores:
    tot_score += score
print(f'Tot Score {tot_score}')
