import PySimpleGUI as sg
susunan = [[sg.VPush("UNISKA MAB", font = ("helvetica",24))],
            [sg.Text("BANJARMASIN", font = ("Courier",18))],
            [sg.VPush()]],
window = sg.Window(title = "elemen Text",
                   layout = susunan,
                   element_justification = "center",
                   size=(430,200))
window.read()
window.close()