import PySimpleGUI as sg
from pathlib import Path

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
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('untitled', key='-DOCNAME-')],
    [sg.Multiline(no_scrollbar=True, size=(80, 30), key='-TEXTBOX-')]
]

window = sg.Window('GUI-Text Editor', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Open':
        file_path = sg.popup_get_file('Open File', no_window=True)
        if file_path:
            file = Path(file_path)
            window['-TEXTBOX-'].update(file.read_text('utf-8'))
            window['-DOCNAME-'].update(file_path.split('/')[-1])

    if event == 'Save':
        file_path = sg.popup_get_file('Save as', no_window=True, save_as=True)
        if file_path[-4:] != '.txt':
            file_path += '.txt'
        file = Path(file_path)
        file.write_text(values['-TEXTBOX-'], encoding='utf-8')
        window['-DOCNAME-'].update(file_path.split('/')[-1])

    if event == 'Word Count':
        full_text = values['-TEXTBOX-']
        clean_text = full_text.replace('\n', '').split(' ')
        word_count = len(clean_text)
        char_count = len(''.join(clean_text))
        sg.popup(f'Words: {word_count}\nCharacters: {char_count}', title='Word Count')

    if event in smiles_events:
        window['-TEXTBOX-'].update(values['-TEXTBOX-'] + ' ' + event)

window.close()
