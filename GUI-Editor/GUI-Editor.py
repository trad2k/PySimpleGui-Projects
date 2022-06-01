import PySimpleGUI as sg

smiles = [
    'happy', [':)', 'xD', ':D', '<3'],
    'sad', [':(', 'T_T'],
    'other', [':3']
]

smiles_events = smiles[1] + smiles[3] + smiles[5]

menu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word Count']],
    ['Add', smiles]
]

sg.theme('GrayGrayGray')
layout =[
    [sg.Menu(menu_layout)],
    [sg.Text('untitled', key='-DOCNAME-')],
    [sg.Multiline(no_scrollbar=True, size = (40, 30), key='-TEXTBOX-')]
]

window = sg.Window('GUI-Text Editor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Word Count':
        print(smiles_events)

window.close()