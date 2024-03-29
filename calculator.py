import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.result_var = tk.StringVar()

        # Display
        self.display = tk.Entry(master, textvariable=self.result_var)
        self.display.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/'
        ]
        row = 1
        col = 0
        for button in buttons:
            tk.Button(master, text=button, command=lambda b=button: self.click(b)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, button):
        if button == "=":
            try:
                self.result_var.set(eval(self.result_var.get()))
            except Exception as e:
                self.result_var.set("Error")
        elif button == "C":
            self.result_var.set("")
        else:
            self.result_var.set(self.result_var.get() + button)
if __name__ == "__main__":
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()
