'''
Intro to writing classes:
'''


class User:
    def __init__(self, user_id, user_name) -> None:
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def folllow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'Jack')
user_2 = User('002', 'Jill')

user_1.folllow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
