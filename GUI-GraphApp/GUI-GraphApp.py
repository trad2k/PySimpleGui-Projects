import PySimpleGUI as sg

sg.theme('DarkTeaL6')

table_content = []
layout = [
    [sg.Table(headings=['Observation', 'Result'],
              values=table_content,
              expand_x=True,
              hide_vertical_scroll=True,
              key='TABLE-')],
    [sg.Input(key='-INPUT-', expand_x=True), sg.Button('Submit')]
]

window = sg.Window('GUI-GraphApp', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        new_value = values['-INPUT-']
        if new_value.isnumeric():
            window['-TABLE-'].update([[1, 10],[2, 12], [3,0]])

window.close()