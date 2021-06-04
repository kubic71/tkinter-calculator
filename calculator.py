import tkinter as tk
import functools

from py_expression_eval import Parser

parser = Parser()


def calculate(str_expr):
    str_expr = str_expr.replace("x", "*")
    return parser.parse(str_expr).evaluate({})


def calculate_and_show(inp, res):
    r = calculate(inp.get())
    res.delete(0, tk.END)
    res.insert(0, r)


button_layout = """( ) % C
7 8 9 /
4 5 6 x
1 2 3 -
0 . = +"""


def my_lambda(button_text):
    return lambda: write_symbol_to_expr_input(button_text)



def write_symbol_to_expr_input(button_text):
    print(button_text)
    if button_text == "C":
        result_entry.delete(0, tk.END)
        expr_input.delete(0, tk.END)
    elif button_text == "=":
        calculate_and_show(expr_input, result_entry)
    else:
        expr_input.insert(tk.END, button_text)



l = []
def create_button_ui():
    for r_i, row in enumerate(button_layout.split("\n")):
        for c_i, button_text in enumerate(row.split()):
            # print((r_i, c_i), button_text)
            # g = lambda: write_symbol_to_expr_input(button_text)
            g = my_lambda(button_text)
            # g = functools.partial(write_symbol_to_expr_input, button_text=button_text)
            l.append(g)
            tk.Button(master, text=button_text, command=g).grid(
                row=r_i, column=c_i, sticky=tk.W
            )




master = tk.Tk()
tk.Label(master, text="Expression").grid(row=5)
tk.Label(master, text="Result").grid(row=6)
create_button_ui()

expr_input = tk.Entry(master)
result_entry = tk.Entry(master)

expr_input.grid(
    row=5,
    column=1,
)
result_entry.grid(row=6, column=1)


tk.Button(master, text="Quit", command=master.quit).grid(
    row=7, column=0, sticky=tk.W, pady=4
)


tk.mainloop()
