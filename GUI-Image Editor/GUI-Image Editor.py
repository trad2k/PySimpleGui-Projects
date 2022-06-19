import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO
from pathlib import Path


def update_image(original, blur, contrast, emboss, contour, flipx, flipy):
    image = original.filter(ImageFilter.GaussianBlur(blur))
    image = image.filter(ImageFilter.UnsharpMask(contrast))

    if emboss:
        image = image.filter(ImageFilter.EMBOSS())
    if contour:
        image = image.filter(ImageFilter.CONTOUR())

    if flipx:
        image = ImageOps.mirror(image)
    if flipy:
        image = ImageOps.flip(image)

    bio = BytesIO()
    image.save(bio, format='PNG')
    window['-IMAGE-'].update(data=bio.getvalue())


image_path = 'test.png'

control_col = sg.Column([
    [sg.Frame('Blur', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-BLUR-')]])],
    [sg.Frame('Contrast', layout=[[sg.Slider(range=(0, 10), orientation='h', key='-CONTRAST-')]])],
    [sg.Checkbox('Emboss', key='-EMBOSS-'), sg.Checkbox('Contour', key='-CONTOUR-')],
    [sg.Checkbox('Flip x', key='-FLIPX-'), sg.Checkbox('Flip Y', key='-FLIPY-')],
    [sg.Button('Save Image', key='-SAVE-')],
])
image_col = sg.Column([[sg.Image(image_path, key='-IMAGE-')]])
layout = [[control_col, image_col]]

original = Image.open(image_path)
window = sg.Window('GUI-Image Editor', layout)

while True:
    event, values = window.read(timeout=100)
    if event == sg.WIN_CLOSED:
        break

    if event == '-SAVE-':
        file_path = sg.popup_get_file('Save as', no_window=True, save_as=True)
        if file_path[-4:] != '.png':
            file_path += '.png'
        file = Path(file_path)
        image.save(file, format='PNG')

    update_image(
        original,
        values['-BLUR-'],
        values['-CONTRAST-'],
        values['-EMBOSS-'],
        values['-CONTOUR-'],
        values['-FLIPX-'],
        values['-FLIPY-']
    )

window.close()