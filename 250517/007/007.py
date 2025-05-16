secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class code :
    def __init__(self, secret_code, meeting_point, time) :
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

ans = code(secret_code, meeting_point, time)
print(f"secret code : {ans.secret_code}")
print(f"meeting point : {ans.meeting_point}")
print(f"time : {ans.time}")