import PySimpleGUI as sg
import sys


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Calibri 16', button_element_size=(6,3))
    button_size = (6,3)
    layout = [
        [sg.Text(
            '0',
            key='-OUTPUT1-',
            font='Calibri 32',
            justification='right',
            expand_x=True,
            pad=(15,0),
            right_click_menu=theme_menu
        )],
        [sg.Button('Enter', expand_x=True), sg.Button('Clear', expand_x=True)],
        [sg.Button('7', size=button_size), sg.Button('8', size=button_size), sg.Button('9', size=button_size), sg.Button('*', size=button_size)],
        [sg.Button('4', size=button_size), sg.Button('5', size=button_size), sg.Button('6', size=button_size), sg.Button('/', size=button_size)],
        [sg.Button('1', size=button_size), sg.Button('2', size=button_size), sg.Button('3', size=button_size), sg.Button('+', size=button_size)],
        [sg.Button('0', expand_x=True), sg.Button('.', size=button_size), sg.Button('-', size=button_size)],
        [sg.Text(f'Running Python v{sys.version:.7}', key='-TEXT1-')]
    ]

    return sg.Window('Calculator', layout)


theme_menu = ['menu', ['DarkBlue8', 'GrayGrayGray', 'DarkAmber', 'DarkBlack', 'Random']]
window = create_window('GrayGrayGray')

current_num = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ['0','1','2','3','4','5','6','7','8','9']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-OUTPUT1-'].update(num_string)

    if event in ['.']:
        if current_num:
            current_num.append(event)
            num_string = ''.join(current_num)
            window['-OUTPUT1-'].update(num_string)

    if event in ['+','-','/','*']:
        if current_num:
            full_operation.append(''.join(current_num))
            current_num = []
            full_operation.append(event)
            window['-OUTPUT1-'].update('0')

    if event == 'Enter':
        if full_operation and full_operation[1]:
            full_operation.append(''.join(current_num))
            result = round(eval(''.join(full_operation)), 10)
            window['-OUTPUT1-'].update(result)
            full_operation = []
            current_num = [str(result)]

    if event == 'Clear':
        window['-OUTPUT1-'].update('0')
        full_operation = []
        current_num = []

window.close()