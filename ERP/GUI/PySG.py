import PySimpleGUI as sg
import pandas as pd
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

# Add color scheme to the window
sg.theme('Kayak')
# params = {'DN': ['DN25', 'DN40', 'DN50'], 'PN': ['PN25', 'PN40'], 'Материал корпуса': ['1.6220', '20ГЛ']}
# print(params)

EXCEL_FILE = 'Data_Entry.xlsx'
df = pd.read_excel(EXCEL_FILE)
print(df)

layout = [
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Name', size=(15, 1)), sg.InputText(key='Name')],
    [sg.Text('City', size=(15, 1)), sg.InputText(key='City')],
    [sg.Text('Favorite colour', size=(15, 1)), sg.Combo(['Green', 'Blue', 'Red'], key='Favorite colour')],
    [sg.Text('I speak', size=(15, 1)),
     sg.Checkbox('German', key='German'),
     sg.Checkbox('Spanish', key='Spanish'),
     sg.Checkbox('English', key='English')],
    [sg.Text('No. of Children', size=(15, 1)), sg.Spin([i for i in range(0, 16)],
                                                       initial_value=0, key='Children')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()],
    # [sg.Combo(value, key=key) for key, value in params.items()]
]

# for key, value in params.items():
#     layout.append([sg.Text(key), sg.Combo(value, key=key)])


window = sg.Window('Simple data entry form', layout)


def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Submit':
        # print(event, values)
        df2 = pd.DataFrame([values])
        df = pd.concat([df, df2], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
        clear_input()
window.close()
