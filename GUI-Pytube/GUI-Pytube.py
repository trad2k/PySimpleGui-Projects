import PySimpleGUI as sg

info_tab = [
    [sg.Text('Title:'), sg.Text('', key='-TITLE-')],
    [sg.Text('Length:'), sg.Text('', key='-LENGTH-')],
    [sg.Text('Views:'), sg.Text('', key='-VIEWS-')],
    [sg.Text('Author:'), sg.Text('', key='-AUTHOR-')],
    [
        sg.Text('Description:'),
        sg.Multiline('', key='-DESCRIPTION-', size=(40,20), no_scrollbar=True, disabled=True)
    ]
]
download_tab = [
    [sg.Frame('Best Quality',
              [[sg.Button('Download', key='-BEST-'), sg.Text('', '-BESTRES-'), sg.Text('', key='-BESTSIZE-')]])],

]

layout = [[sg.TabGroup([[
    sg.Tab('info', info_tab), sg.Tab('download', download_tab)]])]]

window = sg.Window('GUI Pytube', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()