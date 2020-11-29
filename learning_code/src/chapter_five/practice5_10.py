# 检查用户名

current_users = ['M', 'H', 'X', 'spirit', 'mhx']
new_users = ['m', 'L', 'XIAO', 'XIA', 'mhx']
current_users_lower = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(new_user)
        print("this name have been used!\n")
    else:
        print(new_user)
        print("You can use this name~\n")
