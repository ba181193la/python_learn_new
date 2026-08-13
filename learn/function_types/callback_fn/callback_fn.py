def on_button_click(callback):
    print('on_button_click eneter')
    callback()

def show_message():
    print('show_message')

on_button_click(show_message)


def sum(a,b,callback):
    result = a+b
    callback(result)
    return result

def print_result(result):
    print('The result is:', result)

sum(5, 3, print_result)