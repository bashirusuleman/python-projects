import FreeSimpleGUI as sg
from archive import archive_files
import pathlib

# Define the window's contents
# layout = [[sg.Text("Enter Feet:"), sg.Input(key="feet")],
#           [sg.Text("Enter Inches:")],
#           [sg.Button('Convert')]]
#
# # Create the window
# window = sg.Window('Converter', layout)
#
# while True:
#     event , value = window.read()
#     print(value)
#     #if value[0] != int or value[0] != float:
#     print(type(value["feet"]))
#     sg.popup('Enter a float or integer to convert')
#         # window['-OUTPUT-'].update('Enter a float or integer to convert')
#     if event == sg.WINDOW_CLOSED:
#         break
# window.close()


# Define the window's contents
layout = [[sg.Text("Select Files to Compress:"), sg.InputText(), sg.FilesBrowse("Choose Files",key="files")],
          [sg.Text("Select Destination Folder:"),sg.InputText(),  sg.FolderBrowse("Choose Folder", key="folder")],
          [sg.Button('Compress'), sg.Text(key='Output', text_color='black')]]

# Create the window
window = sg.Window('Files Compress', layout)

while True:
    event , value = window.read()
    print(value)
    files = value['files'].split(';')
    folder = value['folder']
    archive_files(files, folder)
    window['Output'].update(value='Files Compressed Successfully!')

    if event == sg.WINDOW_CLOSED:
        break
window.close()

