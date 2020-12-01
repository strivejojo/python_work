# 消息归档
text_list = ['I', 'LOVE', 'YOU', 'MARRY', 'ME']
send_list = []


def show_message(text_lists):
    """打印列表中的文本元素"""
    for text in text_lists:
        print(text)


def send_message(text_lists, send_lists):
    """打印列表的文本，并移动至send_list"""
    while text_lists:
        current_text = text_lists.pop(0)
        print(current_text)
        send_lists.append(current_text)


show_message(text_list)
send_message(text_lists=text_list[:], send_lists=send_list)

print(f"- text_list is {text_list}")
print(f"- send_list is {send_list}")
