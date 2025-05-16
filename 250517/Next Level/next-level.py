user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class info :
    def __init__(self, user2_id = "codetree", user2_level = 10) :
        self.user2_id = user2_id
        self.user2_level = user2_level

answer_1 = info()
print(f"user {answer_1.user2_id} lv {answer_1.user2_level}")
answer_2 = info(user2_id, user2_level)
print(f"user {answer_2.user2_id} lv {answer_2.user2_level}")