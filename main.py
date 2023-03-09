import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry('300x400')
window.title('Calculator')
window.config(bg='#3d3d3c')
ico = Image.open('python_logo.png')
photo = ImageTk.PhotoImage(ico)
window.wm_iconphoto(False, photo)
window.resizable(False, False)

answer_label = tk.Label(window, font='Times 25 bold', anchor='e')
answer_label.pack(fill='both', padx=20, pady=15, ipady=15)

first_num = ""
second_num = ""
option = ""

frame = tk.Frame(window, bg='#3d3d3c')


def create_btn(text, row, column, command, bg):
    btn = tk.Button(frame, bg=bg, fg='white', font='Times 15 bold'
                    , text=text, command=lambda: command(text), height=2, width=4)
    btn.grid(row=row, column=column, padx=5, pady=5, sticky='EW')
    return btn


def set_answer(answer):
    answer_label['text'] = answer;


def clear_all():
    global first_num
    global second_num
    global option

    first_num = ""
    second_num = ""
    option = ""
    set_answer("")


def on_btn_click(btn_text):
    global first_num
    global second_num
    global option

    if btn_text == "C":
        clear_all()
    elif btn_text == "+":
        option = "+"
    elif btn_text == "-":
        option = "-"
    elif btn_text == "*":
        option = "*"
    elif btn_text == "/":
        option = "/"
    elif btn_text == "=":
        if option != "":
            result = 0

            if option == "+":
                result = int(first_num) + int(second_num)
            elif option == "-":
                result = int(first_num) - int(second_num)
            elif option == "*":
                result = int(first_num) * int(second_num)
            elif option == "/":
                result = int(first_num) / int(second_num)

            result = int(result)
            set_answer(result)
            first_num = str(result)
            second_num = ""
            option = ""
    elif first_num != "" and option != "":
        second_num += btn_text
        set_answer(second_num)
    elif second_num == "" and option == "":
        first_num += btn_text
        set_answer(first_num)


create_btn('7', 1, 1, on_btn_click, '#b3b1af')
create_btn('8', 1, 2, on_btn_click, '#b3b1af')
create_btn('9', 1, 3, on_btn_click, '#b3b1af')
create_btn('*', 1, 4, on_btn_click, '#d96e11')

create_btn('4', 2, 1, on_btn_click, '#b3b1af')
create_btn('5', 2, 2, on_btn_click, '#b3b1af')
create_btn('6', 2, 3, on_btn_click, '#b3b1af')
create_btn('/', 2, 4, on_btn_click, '#d96e11')

create_btn('1', 3, 1, on_btn_click, '#b3b1af')
create_btn('2', 3, 2, on_btn_click, '#b3b1af')
create_btn('3', 3, 3, on_btn_click, '#b3b1af')
create_btn('+', 3, 4, on_btn_click, '#d96e11')

create_btn('0', 4, 1, on_btn_click, '#b3b1af')
create_btn('=', 4, 2, on_btn_click, '#d96e11')
create_btn('C', 4, 3, on_btn_click, '#d96e11')
create_btn('-', 4, 4, on_btn_click, '#d96e11')

frame.pack(expand=True, anchor="s", ipady=10)
window.mainloop()
