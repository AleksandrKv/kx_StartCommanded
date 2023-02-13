import tkinter as tk
import tkinter.messagebox as mb
import subprocess  
import json
import os.path as os


def btn_click(ind):
    print(ind)
    # mb.showinfo(title='Мой заголовок', message=command_list[ind]["command"])
    command = command_list[ind]["command"]
    param = command_list[ind]["param"]
    if command == 'start_exe':
        subprocess.Popen(param)

command_list = [
    {
        "name": "name1", 
        "caption": "Проверить наличие файлов в архиве", 
        "command": "start_exe",
        "param": "C:\\Windows\\System32\\notepad.exe D:\\tmp\\tmp.txt",
        "close": True},
    {
        "name": "name2", 
        "caption": "Открыть проект/задачу/папку", 
        "command": "start_exe",
        "param": "d:\\ProgramData\\utilities\\OpenTaskOrFolder\\main.exe",
        "close": True},
]

prog_params = {
    'window_width': 400,
    'window_height': 250,
    'commands_list': command_list,
}
filename = 'prog_params.json'
if os.exists(filename):
    pass

with open(filename, 'w', encoding='utf-8') as fp:
    json.dump(prog_params, fp, indent=4, ensure_ascii=False)

win = tk.Tk()
win.title('Помощник windows - StartCommander')
win.geometry(f'{prog_params["window_width"]}x{prog_params["window_height"]}')
win.resizable(width=False, height=False) # возможность изменять размеры окна


frame = tk.Frame()
frame.pack()
frame.columnconfigure(0, minsize=prog_params['window_width'])

buttons = []
for ind,val in enumerate(command_list):
    btn = tk.Button(frame, text=val["caption"], bd=3, command=lambda i=ind: btn_click(i), name=val["name"])
    btn.grid(row=ind, column=0, stick="wens", padx=10, pady=3)
    buttons.append(btn)
    frame.rowconfigure(ind, minsize=40)

win.mainloop()
