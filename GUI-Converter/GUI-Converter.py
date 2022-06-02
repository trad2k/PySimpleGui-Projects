import PySimpleGUI as sg
import sys

layout = [
    [sg.Input(key='-INPUT1-')],
    [sg.Combo(['km to mile', 'kg to pound', 'sec to min'], key='-UNITS1-', default_value='km to mile')],
    [sg.Button('Convert', key='-CONVERT1-')],
    [sg.Text('Output', key='-OUTPUT1-')],
    [sg.Text(f'Running Python v{sys.version:.7}', key='-TEXT1-')]
]

window = sg.Window('GUI-Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT1-':
        input_value = values['-INPUT1-']
        if input_value.isnumeric():
            match values['-UNITS1-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.6214,2)
                    output_string = f'{input_value} km are {output} miles.'
                case 'kg to pound':
                    output = round(float(input_value) * 2.20462,2)
                    output_string = f'{input_value} kg are {output} pounds.'
                case 'sec to min':
                    output = round(float(input_value) / 60,2)
                    output_string = f'{input_value} seconds are {output} minutes.'

            window['-OUTPUT1-'].update(output_string)
        else:
            window['-OUTPUT1-'].update('Please enter a number')

window.close()