import PySimpleGUI as sg

sg.theme('DarkTeaL6')

table_content = []
layout = [
    [sg.Table(headings=['Observation', 'Result'],
              values=table_content,
              expand_x=True,
              hide_vertical_scroll=True,
              key='-TABLE-')],
    [sg.Input(key='-INPUT-', expand_x=True), sg.Button('Submit')]
]

window = sg.Window('GUI-GraphApp', layout)

observ_num = 0

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        new_value = values['-INPUT-']
        if new_value.isnumeric():
            observ_num +=1
            table_content.append([observ_num, new_value])
            window['-TABLE-'].update(table_content)
            window['-INPUT-'].update('')

window.close()