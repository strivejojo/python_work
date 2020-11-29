# 处理没有用户的情形
user_lists = []
if user_lists:
    for user in user_lists:
        if user == 'admin':
            print(f"Hello {user},would you like to see a status report?")
        else:
            print(f"Hello {user},thank you for logging in again.")
else:
    print("We need to find some users!")
