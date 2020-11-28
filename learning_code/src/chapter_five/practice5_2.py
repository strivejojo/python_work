# 更多条件测试

#检查两个字符串相等和不等
char01 = 'I love you'
char02 = 'I like you'
char03 = 'I need you'
char04 = 'I need you'
print(char01 == char02)
print(char03 == char04)
print('\n')

#使用方法lower()的测试
name = 'JOjo'
print(name.lower() == 'jojo')
print(name)
print('\n')

#测试特定的值是否包含在列表中
list = ['jojo', 'whiskey', 'conflict']
print('jojo' in list)
print('linkin park' not in list)
print('badminton' in list)
