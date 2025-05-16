unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class info :
    def __init__(self,unlock_code,wire_color,seconds) :
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

ans = info(unlock_code,wire_color,seconds)
print(f"code : {ans.unlock_code}")
print(f"color : {ans.wire_color}")
print(f"second : {ans.seconds}")