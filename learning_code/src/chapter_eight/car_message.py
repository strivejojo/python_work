"""与创建汽车信息有关的函数"""


def make_car(manufacturer, model, **car_options):
    """创建一个表示汽车的字典"""
    car_dict ={
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in car_options.items():
        car_dict[option] = value
    return car_dict
