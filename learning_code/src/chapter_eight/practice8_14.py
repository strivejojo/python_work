# 汽车
def car_message(manufacturer, model, **car_options):
    """创建一个表示汽车的字典"""
    car_dict ={
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in car_options.items():
        car_dict[option] = value
    return car_dict


car = car_message('subaru', 'outback', color='blue', tow_package=True)
print(car)
