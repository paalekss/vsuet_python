import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def calculator():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Ошибка", "Деление на ноль невозможно")
                return
            result = num1 / num2
        result_label.config(text=f" = {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа")

def show_selection():
    selections = ''
    if var1.get():
        selection = "первый"
    if var2.get():
        selection = "второй"
    if var3.get():
        selection = "третий"
    if selection != '':
        messagebox.showinfo("Выбор", f"Вы выбрали {selection} вариант")
    else:
        messagebox.showinfo("Выбор", "Вы не выбрали вариант")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

root = tk.Tk()
root.geometry('500x200')
root.title("Пудинова Александра Вадимовна")  

notebook = ttk.Notebook(root)
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)
notebook.add(tab1, text="Простой калькулятор")
notebook.add(tab2, text="Выбор чекбокса")
notebook.add(tab3, text="Работа с текстом")
notebook.pack(expand=True, fill="both")

entry1 = tk.Entry(tab1)
entry1.pack(pady=7)
entry1.grid(row=0,column=0)

operation_var = tk.StringVar(value="+")
operation_menu = tk.OptionMenu(tab1, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=0,column=1)

entry2 = tk.Entry(tab1)
entry2.grid(row=0,column=2)

calculate_button = tk.Button(tab1, text="Вычислить", command=calculator)
calculate_button.grid(row=1,column=1)

result_label = tk.Label(tab1, text=" = ")
result_label.grid(row=0,column=3)

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

checkbox1 = tk.Checkbutton(tab2, text="Первый", variable=var1)
checkbox1.pack(pady=5)
checkbox2 = tk.Checkbutton(tab2, text="Второй", variable=var2)
checkbox2.pack(pady=5)
checkbox3 = tk.Checkbutton(tab2, text="Третий", variable=var3)
checkbox3.pack(pady=5)

show_button = tk.Button(tab2, text="Выбрать вариант", command=show_selection)
show_button.pack(pady=5)

text_area = tk.Text(tab3)
text_area.pack(expand=True, fill="both", padx=5, pady=5)

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Открыть файл", command=open_file)
menu_bar.add_cascade(label="Файл", menu=file_menu)
root.config(menu=menu_bar)
root.mainloop()