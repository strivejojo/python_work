"""与打印 3D 模型相关的函数。 """


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止。
    打印每个设计后，都将其移到列表 completed_models 中。
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作 3D 打印模型的过程。
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型。 """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
