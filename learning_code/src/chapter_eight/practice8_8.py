# 用户的专辑
def make_album(singer, album_name, number=None):
    """创建一个包含专辑信息的字典"""
    one_album = {'singer': singer,
                 'ablum_name': album_name,
                 }
    if number:
        one_album['number'] = number
    return one_album

while True:
    singer_name = input("\nPlease enter the name of a singer: \n"
                        "(enter 'q' at any time to quit)")
    if singer_name == 'q':
        break

    album_name = input("\nPlease enter the name of the album: \n"
                       "(enter 'q' at any time to quit)")
    if album_name == 'q':
        break

    user_album = make_album(singer_name, album_name)
    print(user_album)
    print('\n')
