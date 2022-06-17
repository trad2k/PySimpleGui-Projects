import PySimpleGUI as sg
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def update_figure(data):
    axes = fig.axes
    x = [i[0] for i in data]
    y = [int(i[1]) for i in data]
    axes[0].plot(x,y,'r-')
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()

sg.theme('DarkTeaL6')

table_content = []
layout = [
    [sg.Table(headings=['Observation', 'Result'],
              values=table_content,
              expand_x=True,
              hide_vertical_scroll=True,
              key='-TABLE-')],
    [sg.Input(key='-INPUT-', expand_x=True), sg.Button('Submit')],
    [sg.Canvas(key='-CANVAS-')]
]

window = sg.Window('GUI-GraphApp', layout, finalize=True)

observ_num = 0

# matplotlib
fig = matplotlib.figure.Figure(figsize=(5, 4))
fig.add_subplot(111).plot([],[])
figure_canvas_agg = FigureCanvasTkAgg(fig,window['-CANVAS-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        new_value = values['-INPUT-']
        if new_value.isnumeric():
            observ_num +=1
            table_content.append([observ_num, float(new_value)])
            window['-TABLE-'].update(table_content)
            update_figure(table_content)
            window['-INPUT-'].update('')

window.close()