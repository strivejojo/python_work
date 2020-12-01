# 专辑
def make_album(singer, album_name, number=None):
    """创建一个包含专辑信息的字典"""
    one_album = {'singer': singer,
                 'ablum_name': album_name,
                 }
    if number:
        one_album['number'] = number
    return one_album


album = make_album('metallica', 'ride the lightning')
print(album)
album = make_album('beethoven', 'ninth symphony')
print(album)
album = make_album('willie nelson', 'red-headed stranger')
print(album)
album = make_album('iron maiden', 'piece of mind', number=8)
print(album)
