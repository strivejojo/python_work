# 以特殊方式跟管理员打招呼
user_lists = ['M', 'H', 'X', 'admin', 'mhx']
for user in user_lists:
    if user == 'admin':
        print(f"Hello {user},would you like to see a status report?")
    else:
        print(f"Hello {user},thank you for logging in again.")
